import os
import subprocess
import logging

NO_NEWLINE = 25
logging.addLevelName(NO_NEWLINE, "NO_NEWLINE")

class NoNewLineHandler(logging.StreamHandler):
    def emit(self, record):
        msg = self.format(record)
        if record.levelno == NO_NEWLINE:
            self.stream.write(msg)
        else:
            self.stream.write(msg + "\n")
        self.flush()

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[NoNewLineHandler()]
)

logger = logging.getLogger()

class FilesCompiler:
    def __init__(self):
        self.forms_dir = os.path.join(os.path.dirname(__file__), '..', 'forms')
        self.qrc_dir = os.path.join(os.path.dirname(__file__), '..', 'src', 'meta_app', 'ui', 'images')
        self.views_dir = os.path.join(os.path.dirname(__file__), '..', 'src', 'meta_app', 'ui', 'views')
        self.for_replace = {
            'import images_rc': 'from meta_app.ui.views import images_rc\n'
        }
        self.replace_queue = []

        os.makedirs(self.views_dir, exist_ok=True)

        self.ui_files = [f for f in os.listdir(self.forms_dir) if f.endswith('.ui')]
        self.qrc_files = [f for f in os.listdir(self.qrc_dir) if f.endswith('.qrc')]

    def ui_compiling(self) -> None:
        logging.info("Компиляция файлов ui")
        for ui_file in self.ui_files:
            ui_path = os.path.join(self.forms_dir, ui_file)
            py_file = ui_file.replace('.ui', '.py')
            py_path = os.path.join(self.views_dir, py_file)

            logging.log(NO_NEWLINE, f"Компиляция: {ui_file} -> {py_file} ")
            try:
                subprocess.run(['pyside6-uic', '-o', py_path, ui_path])
                logging.info(f"+")
                self.replace_queue.append(py_path)
            except Exception as e:
                logging.info("-")

    def qrc_compiling(self) -> None:
        logging.info("Компиляция файлов qrc")
        for qrc_file in self.qrc_files:
            qrc_path = os.path.join(self.qrc_dir, qrc_file)
            py_file = qrc_file.replace('.qrc', '_rc.py')
            py_path = os.path.join(self.views_dir, py_file)

            logging.log(NO_NEWLINE,f"Компиляция: {qrc_file} -> {py_file} ")
            try:
                subprocess.run(['pyside6-rcc', '-o', py_path, qrc_path])
                logging.info(f"+")
            except Exception as e:
                logging.info(f"-")

    def images_rc_fix(self) -> None:
        for file_path in self.replace_queue:
            self.file_rc_rewrite(file_path)

    def file_rc_rewrite(self, path) -> None:
        logging.info("Фикс")
        with open(path, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            for k, v in self.for_replace.items():
                if k in line:
                    logging.log(NO_NEWLINE, f"Перезапись строки: {lines[i]} -> {v} ")
                    lines[i] = v
                    logging.info(f"+")

        with open(path, "w") as file:
            file.writelines(lines)

    def execute(self):
        logging.info("Запуск")
        self.qrc_compiling()
        self.ui_compiling()
        self.images_rc_fix()

compiler = FilesCompiler()
compiler.execute()
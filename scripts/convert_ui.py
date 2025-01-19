import os
import subprocess

forms_dir = os.path.join(os.path.dirname(__file__), '..', 'forms')
views_dir = os.path.join(os.path.dirname(__file__), '..', 'meta_app', 'ui', 'views')

os.makedirs(views_dir, exist_ok=True)

ui_files = [f for f in os.listdir(forms_dir) if f.endswith('.ui')]

for ui_file in ui_files:
    ui_path = os.path.join(forms_dir, ui_file)
    py_file = ui_file.replace('.ui', '.py')
    py_path = os.path.join(views_dir, py_file)

    subprocess.run(['pyside6-uic', '-o', py_path, ui_path])
    print(f"Скомпилирован: {ui_file} -> {py_file}")

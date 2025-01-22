from PIL import Image
from PIL.ExifTags import TAGS


def get_photo_data(file_path):
    """
    :param file_path: Путь к файлу
    :return: Словарь с метаданными
    """
    metadata = {}
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                for tag_id, value in exif_data.items():
                    tag_name = TAGS.get(tag_id, tag_id)
                    print(f"{tag_name}: {value}")
                    metadata[tag_name] = value
            else:
                metadata["Ошибка"] = "Файл не содержит EXIF-данных"

    except Exception as e:
        metadata["Ошибка"] = str(e)

    return metadata



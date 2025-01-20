# from exif import Image
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
            # Получаем словарь с EXIF-данными
            exif_data = img._getexif()
            if exif_data is not None:
                for tag_id, value in exif_data.items():
                    tag_name = TAGS.get(tag_id, tag_id)
                    print(f"{tag_name}: {value}")
                    metadata[f"{str(tag_name)[:20]}..."] = f"{str(value)[:20]}..."
            else:
                metadata["Ошибка"] = "Файл не содержит EXIF-данных"

    except Exception as e:
        metadata["Ошибка"] = str(e)

    return metadata

    # with open(file_path, "rb") as file:
    #     file_image = Image(file)
    #
    # images = [file_image]
    #
    # for index, image in enumerate(images):
    #     if image.has_exif:
    #         status = f"содержит информацию EXIF (версии {image.exif_version})"
    #     else:
    #         status = "Не содержит информации EXIF"
    #     print(f"Изображение {index} {status}")
    #
    # metadata = {}
    #
    # for index, image in enumerate(images):
    #     metadata["Make"] = image.make
    #     metadata["Model"] = image.model
    #
    # return metadata

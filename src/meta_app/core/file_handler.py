from PIL import Image
from PIL.ExifTags import TAGS
import piexif

def update_exif_data(file_path, updated_metadata):
    img = Image.open(file_path)
    exif_data = piexif.load(img.info.get("exif", b""))

    if not exif_data:
        raise ValueError("EXIF данные отсутствуют в файле.")

    tags = {}
    for ifd in exif_data:
        if ifd in ["0th", "Exif", "GPS"]:
            for tag_id, tag_value in exif_data[ifd].items():
                try:
                    tag_name = piexif.TAGS["Image"][tag_id]["name"]
                    tags[tag_name] = (ifd, tag_id)
                except KeyError:
                    continue

    for key, value in updated_metadata.items():
        if key in list(tags):
            ifd, tag_id = tags[key]
            try:
                current_value = exif_data[ifd][tag_id]

                if isinstance(current_value, tuple) and len(current_value) == 2:
                    current_value = current_value[0] / current_value[1]

                if current_value != value:
                    exif_data[ifd][tag_id] = value
                    print(f"Обновлено: {key} = {value}")
            except Exception as e:
                print(f"Не удалось обновить {key}: {e}")

    exif_bytes = piexif.dump(exif_data)
    img.save(file_path, exif=exif_bytes)

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
                    metadata[tag_name] = value
            else:
                metadata["Ошибка"] = "Файл не содержит EXIF-данных"

    except Exception as e:
        metadata["Ошибка"] = str(e)

    return metadata



from PIL import Image
from PIL.ExifTags import TAGS
import piexif

def update_exif_data(file_path, updated_metadata):
    img = Image.open(file_path)
    exif_data = piexif.load(img.info.get("exif", b""))

    if not exif_data:
        raise ValueError("EXIF данные отсутствуют в файле.")

    exif_dict = {TAGS.get(tag, tag): value for tag, value in img._getexif().items()}

    for key, value in updated_metadata.items():
        print(f"{key} in exif_dict check")
        if key in list(exif_dict):
            print("KEY IN")
            for ifd in exif_data:
                if ifd == "0th" or ifd == "Exif" or ifd == "GPS":
                    print("IN DATA")
                    tags = {}
                    for tag_id, tag_value in exif_data[ifd].items():
                        # print(piexif.TAGS)
                        try:
                            tags[piexif.TAGS["Image"][tag_id]["name"]] = tag_id
                        except KeyError:
                            continue
                    if key in list(tags) and key != "IFDRational":
                        print(f"TAG {key} IN")
                        tag_inx = tags[key]
                        try:
                            # if updated_metadata[key] != exif_data[ifd][tag_inx]:
                            exif_data[ifd][tag_inx] = value
                            # print(f"Обновлено: {key}")
                        except Exception as e:
                            print(f"Не удалось обновить: {e}")

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



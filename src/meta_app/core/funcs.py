import webbrowser

def open_url(data):
    link = create_map_link(data)
    print(link)
    webbrowser.open(link)

def dms_to_decimal(dms):
    degrees, minutes, seconds = dms
    decimal = float(degrees) + (float(minutes) / 60) + (float(seconds) / 3600)
    return decimal

def create_map_link(data: dict):
    latitude_dms = data[2]
    longitude_dms = data[4]
    latitude_direction = data[1]
    longitude_direction = data[3]

    latitude = dms_to_decimal(latitude_dms)
    longitude = dms_to_decimal(longitude_dms)

    if latitude_direction == 'S':
        latitude = -latitude
    if longitude_direction == 'W':
        longitude = -longitude

    return f"https://www.google.com/maps?q={latitude},{longitude}"



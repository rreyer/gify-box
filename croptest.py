from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()

# Kamera-Konfiguration abrufen
config = picam2.create_preview_configuration()

# Hole aktuelle sensor size (z. B. 2304x1296 bei HQ-Kamera)
sensor_resolution = config["main"]["size"]
sensor_width, sensor_height = sensor_resolution

# Zielverhältnis 16:9 berechnen (Crop)
crop_width = sensor_width
crop_height = int(sensor_width * 9 / 16)

# Wenn Höhe zu groß ist, lieber Breite anpassen
if crop_height > sensor_height:
    crop_height = sensor_height
    crop_width = int(sensor_height * 16 / 9)

# Crop-Startpunkt mittig
crop_x = (sensor_width - crop_width) // 2
crop_y = (sensor_height - crop_height) // 2

# Crop setzen
config["transform"] = picam2.Transform(hflip=0, vflip=0)
config["main"]["crop"] = (crop_x, crop_y, crop_width, crop_height)

# Konfiguration anwenden
picam2.configure(config)

# Starte Preview
picam2.start_preview(Preview.QTGL)  # Oder Preview.NULL, Preview.DRM
picam2.start()

time.sleep(100)  # Oder Endlosschleife
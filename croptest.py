from picamera2 import Picamera2, Preview
from libcamera import Transform
import time

picam2 = Picamera2()

# Kamera-Konfiguration abrufen
config = picam2.create_preview_configuration()

print(picam2.camera_controls["ScalerCrop"])

# Hole aktuelle sensor size (z. B. 2304x1296 bei HQ-Kamera)
sensor_resolution = config["main"]["size"]
sensor_width, sensor_height = sensor_resolution

print(sensor_resolution, sensor_width, sensor_height)

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

config = picam2.create_preview_configuration(controls={"ScalerCrop": (crop_x, crop_y, crop_width, crop_height)})
# Konfiguration anwenden
picam2.configure(config)

# Starte Preview
picam2.start_preview(Preview.QT, x=0, y=0, height=1080, width=1920, transform=Transform(hflip=1))
picam2.start()

time.sleep(100)  # Oder Endlosschleife
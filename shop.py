# Logica de la aplicación
import cv2
from ultralytics import YOLO
import math

class TiendaInteligente:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)

        # Modelos
        ObjectModel = YOLO()
        self.ObjectModel = ObjectModel

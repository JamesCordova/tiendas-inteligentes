# Logica de la aplicación
import cv2
from ultralytics import YOLO
import math

class TiendaInteligente:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

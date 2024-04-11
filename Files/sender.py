import cv2
import numpy as np
import socket
import base64


MAX_DGRAM = 2**16
MAX_IMAGE_DGRAM = MAX_DGRAM - 64 # extract 64 bytes in case UDP frame overflown

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_port = 12345
dest_ip = "127.0.0.1"


def send_frame(img):
    compressed = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 80])[1]
    data = base64.b64encode(compressed)
    s.sendto(data, (dest_ip, dest_port))

cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    _, frame = cap.read()
    send_frame(frame)
cap.release()
cv2.destroyAllWindows()
s.close()
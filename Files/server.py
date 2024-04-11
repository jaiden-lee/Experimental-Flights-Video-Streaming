import cv2
import numpy as np
import socket
import base64

MAX_DGRAM = 2**16
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_ip = "127.0.0.1"
host_port = 12345
s.bind((host_ip, host_port))

while True:
    packet, addr = s.recvfrom(MAX_DGRAM)
    data = base64.b64decode(packet, ' /')
    npdata = np.fromstring(data, dtype=np.uint8)
    frame = cv2.imdecode(npdata, 1)
    cv2.imshow("RECEIVING VIDEO", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        socket.close()
        break
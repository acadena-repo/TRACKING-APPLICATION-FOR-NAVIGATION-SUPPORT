import socket
from math import ceil


class Sensor:
    def __init__(self):
        self.loc = {'x': 0, 'y': 0, 'xn': 0, 'yn': 0,
                    'dx': 0, 'dy': 0, 'orientation': 0}
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 7932
        self.addr = (self.server, self.port)
        self.start = self.connect()

    def get_location(self, pose):
        pos = [float(p) for p in pose.split()]
        self.loc['x'] = ceil(pos[0]*10)  # Value converted to pixels
        self.loc['y'] = ceil(pos[1]*10)  # Value converted to pixels
        self.loc['orientation'] = ceil(pos[2])
        self.loc['dx'] = ceil(
            self.loc['xn'] - self.loc['x'])  # Value in pixels
        self.loc['dy'] = ceil(
            self.loc['yn'] - self.loc['y'])  # Value in pixels
        # memorize last value
        self.loc['xn'] = self.loc['x']
        self.loc['yn'] = self.loc['y']

    def connect(self):
        try:
            self.client.connect(self.addr)
            response = self.client.recv(1024).decode()
            self.get_location(response)
            return self.loc
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            response = self.client.recv(1024).decode()
            self.get_location(response)
            return self.loc
        except socket.error as e:
            print(e)

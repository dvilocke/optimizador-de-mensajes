import time

from base import Base

import pywhatkit
import win32clipboard
import random

class Girlfriend(Base):

    NUMBER = '+573155940298';

    message_list = [
        'Buenos dias amor de mi vida',
        'Buenos dias preciosa',
        'Buenos dias amor de mi vida, estas muy rica',
        'Buenos dias mi amor, Te quiero mi vida',
        'Buenos dias amor, quiero hacerte muchas cosas ricas'
    ]
    img = [
        '\imagen1.jpg',
        '\imagen2.jpg'
    ]

    def run(self):
        pywhatkit.sendwhatmsg_instantly(self.NUMBER, random.choice(self.message_list))
        #send an image
        path = r'C:\Users\lenov\PycharmProjects\proyecto mensajes\imagenes'
        path_complete = path + random.choice(self.img)
        time.sleep(10)
        pywhatkit.sendwhats_image(self.NUMBER, path_complete)

    def time(self):
        #run at 7 am
        return 7

    def can_run(self):
        return True



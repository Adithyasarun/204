import socket
from tkinter import *
from  threading import Thread
import random


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 8000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=recivedMsg)
    thread.start()

    askPlayerName()


def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEnt ry
    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy( )
    
    SERVER.send(playe rName. encode ( ) )


setup()
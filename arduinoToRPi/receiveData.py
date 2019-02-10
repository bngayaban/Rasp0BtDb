## tutorial for bt
# http://www.uugear.com/portfolio/bluetooth-communication-between-raspberry-pi-and-arduino/

# bt to python reference
# https://pythonhosted.org/pyserial/pyserial_api.html#module-functions-and-attributes

#parsing bytes to char and ints n stuff
# https://www.devdungeon.com/content/working-binary-data-python#bytes

import serial
from time import sleep
import sys

sys.path.append('Db/')

import database as db

bluetoothSerial = serial.Serial("/dev/rfcomm1", baudrate=9600)

nBytes = 256

while(True):
    rawData = bytearray() #byte array
    while(in_waiting() > 0):
        last = bluetoothSerial.read(1)
        rawData.append(last)
    if last.decode("ascii") != "\n":
        print("Error: Bluetooth read, no newline found\n")

    parse(rawData)
    sleep(5) #sleep 5 seconds

def parse(data):

    decodedData = data.decode("ascii")

    "".join(decodedData.split()) #remove all whitespace
    decodedData.replace(":", ",") # replace : with ,
    decodedData.split(",") # split by comma

    dataDict = dict(zip(decodedData[::2], decodedData[1::2])) #converts to dictionry ie key:temp, value:actualTemp

    db.insert(gas=dataDict.get('g', -1),
                lightIntensity=dataDict.get('li', -1),
                temperature =dataDict.get('t', -1.0),
                humidity=dataDict.get('h', -1.0),
                pressure=dataDict.get('p_hg', -1.0),
                c02_level=dataDict.get('c', -1.0),
                soil_moisture=dataDict.get('g', -1.0),
                waterPresence=dataDict.get('w', "-1"))

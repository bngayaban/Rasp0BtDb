# sqlite3 documentation
# https://docs.python.org/3.7/library/sqlite3.html#

import sqlite3 # should be included by default in newer versions of python


def init():
    db = getConnection()
    db.execute('''CREATE TABLE IF NOT EXISTS plantData
                (gas INTEGER,
                lightIntensity INTEGER,
                temperature REAL,
                humidity REAL,
                pressure REAL,
                c02_level REAL,
                soil_moisture REAL,
                water TEXT)''')
    closeDB(db)


def getConnections():
    db = sqlite3.connect("smartPot.db")
    return db

def closeDB(db):
    db.commit()
    db.close()

def insert( gas=-1,
            lightIntensity=-1,
            temperature = -1.0,
            humidity=-1.0,
            pressure=-1.0,
            c02_level=-1.0,
            soil_moisture=-1.0,
            waterPresence="-1"):

    db = getConnections()

    db.execute("INSERT INTO plantData values(?,?,?,?,?,?,?)",
            (gas, lightIntensity, temperature, humidity, pressure, c02_level, soil_moisture, waterPresenece))

    closeDB(db)

def read():
    db = getConnections()

    db.execute("SELECT * FROM plantData")

    all_rows = db.fetchall()

    closeDB(db)

    return all_rows

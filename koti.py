from datetime import date, timedelta
import os
from pymongo import MongoClient
import Adafruit_BMP.BMP085 as BMP085
from datetime import datetime

FREQUENCY_SECONDS = 30


def main():
    client = MongoClient(
        'mongodb+srv://'
        + os.environ['KOTI_CONNECTION_USER']
        + ':'
        + os.environ['KOTI_CONNECTION_PWD']
        + '@'
        + os.environ['KOTI_CONNECTION']
        + '/?retryWrites=true&w=majority'
    )

    db = client.environment

    from pprint import pprint

    pprint(db.collection.find(
        {
            'date': {
                '$lt': datetime.datetime.now(),
                '$gt': datetime.datetime.now() - timedelta(hours=24),
            }
        }
    ))

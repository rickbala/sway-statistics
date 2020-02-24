import pymongo
import datetime
from dateutil.relativedelta import *

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["swaydb"]
mycol = mydb["swaycol"]

yesterday = relativedelta(days=-1)
myquery = {"date" : {"$gt":datetime.datetime.now()+yesterday} }

myresult = mycol.find(myquery).sort("channel", 1)

for result in myresult:
	print(result["channel"])

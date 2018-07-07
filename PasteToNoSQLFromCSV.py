import pymongo
import sys
import csv

def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.basa
    user_csv_collection = db.data
    
    csvfile = open('./dataset.csv')
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #csvreader.__next__()
    
    for i in csvreader:
        user_csv_collection.insert({
            "credit_card": i[0],
            "currency": i[1],
            "catch_phrase":i[2],
            "fda_ndc_code": i[3]
        })

if __name__ == "__main__":
    main()

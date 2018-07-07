import pymongo
import sys
import xml.etree.ElementTree as ET

def parseXML(file):
    tree = ET.parse(file)
    root = tree.getroot()
    
    result = []

    for record in root.findall('record'):
        result.append({
            'credit_card':  record.find('credit_card').text,
            'currency': record.find('currency').text,
            'catch_phrase': record.find('catch_phrase').text,
            'fda_ndc_code': record.find('fda_ndc_code').text
        })

    return result
    
    
def main():
    client = pymongo.MongoClient('localhost', 27017)
    
    db = client.basa
    
    data_collection = db.data
    
    for i in parseXML('dataset.xml'):
        data_collection.insert({
            "credit_card": i["credit_card"],
            "currency": i["currency"],
            "catch_phrase": i["catch_phrase"],
            "fda_ndc_code": i["fda_ndc_code"]
        })


if __name__ == "__main__":
    main()

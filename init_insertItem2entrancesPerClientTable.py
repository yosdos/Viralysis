from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import boto3
from boto3.dynamodb.conditions import Key, Attr
from HandleItems import RawDataProcessing, InsertItem2entrancesPerClientTable
import json

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
mainTable = dynamodb.Table('AllDataViralysis')

def handleItem(item):
    RawDataProcessing.rawDataProcessing(item)
    InsertItem2entrancesPerClientTable.insertItem2entrancesPerClientTable(item)

items = mainTable.scan()['Items']
with ThreadPoolExecutor(max_workers = 20) as executor:
    executor.map(handleItem, items)

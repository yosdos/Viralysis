import boto3
from boto3.dynamodb.conditions import Key, Attr
import decimal
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
entrancesPerClientTable = dynamodb.Table('entrancesPerClient')

def insertItem2entrancesPerClientTable(item):
    if not item['fromOutSide'] or \
	not item['legalViralysisClientId'] or \
	not item['info']['insertItem2entrancesPerClientTable']: return
    new_item = {'client' : item['ViralysisClientId'],\
                'time' : item['dateTimestamp'],\
                'fromSharing' : int(item['vai'] != ''),\
                'userUnidentified' : int(item['userUnidentified']),\
               'fromSharingAndUserUnidentified' : int(item['vai'] != '' and item['userUnidentified']),\
               'entrances': 1}
    try:
        entrancesPerClientTable.put_item(\
                    Item=new_item, \
                    ConditionExpression = "attribute_not_exists(client)")
    except:
        try:
            entrancesPerClientTable.update_item(
                Key={
                    'client': new_item['client'],
                    'time': decimal.Decimal(new_item['time'])
                },
                UpdateExpression='set fromSharing = fromSharing + :v1, ' + \
                                'userUnidentified = userUnidentified + :v2, ' + \
                                'fromSharingAndUserUnidentified = fromSharingAndUserUnidentified + :v3, ' + \
                                'entrances = entrances + :v4',
                ExpressionAttributeValues={
                    ':v1': decimal.Decimal(new_item['fromSharing']),
                    ':v2': decimal.Decimal(new_item['userUnidentified']),
                    ':v3': decimal.Decimal(new_item['fromSharingAndUserUnidentified']),
                    ':v4' : 1
                },
                ReturnValues="UPDATED_NEW")
        except:
            pass


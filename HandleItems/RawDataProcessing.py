import json
import decimal
from datetime import timezone,datetime
import boto3
from boto3.dynamodb.conditions import Key, Attr
import json


roundStrTimestamp = lambda t: decimal.Decimal(datetime(*datetime.fromtimestamp(float(t),timezone.utc).timetuple()[:3], tzinfo=timezone.utc).timestamp())
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
clientsTable = dynamodb.Table('clients')


def rawDataProcessing(item):
    body = json.loads(item['body-json'].replace('\'','\"'))
    item['href'] = body['href']
    item['vai'] = body['vai']
    item['ViralysisClientId'] = body['ViralysisClientId']
    item['userUnidentified'] = (body['ViralysisId'] == '')
    item['referrer'] = 'EMPTY' if 'referrer' not in body or body['referrer'] == '' else body['referrer']
    item['fromOutSide'] = item['href'].split('//')[1].split('/')[0] not in item['referrer']
    item['dateTimestamp'] = roundStrTimestamp(item['time'])
    item['info'] = clientsTable.get_item(Key={'ID': item['ViralysisClientId']})
    if 'Item' in item['info']:
        item['info'] = item['info']['Item']
        item['legalViralysisClientId'] = True
    else:
        item['info'] = None
        item['legalViralysisClientId'] = False


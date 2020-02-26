# %load DeleteItems.py

def DeleteItems(Table):
    '''
    Delete all the item in given table
    '''
    import boto3
    print('deleting items in feed table')
    dynamodb = boto3.resource('dynamodb')
    Feed_table = dynamodb.Table(Table)
    Feed_tableS = Feed_table.scan()
    for each in Feed_tableS.get('Items'):
        Feed_table.delete_item(Key={'time': each['time']})

    print('Done to delete all items in feed table ({})'.format(Table))

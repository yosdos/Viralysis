
def Add_Items_And_Delete_Items():
    import boto3
    import pandas as pd
    
    dynamodb = boto3.resource('dynamodb')
    Feed_table = dynamodb.Table('viralysisTable1')
    Data_table = dynamodb.Table('AllDataViralysis')

    Feed_tableS = Feed_table.scan()
    Feed_tableS.get('Items')
    Pandas_Feed_table = pd.DataFrame.from_dict(Feed_tableS.get('Items'))

    #     Get the new feed and put them in the new table
    for each in Feed_tableS.get('Items'):
        print('Adding items from feed table (viralysisTable1) to DataTable (AllDataViralysis)... ')
        Data_table.put_item(Item=each)
        
        print('Deleting all ''old'' items from feed table (viralysisTable1)')
        Feed_table.delete_item(Key={'time': each['time']})
        
        print('Done deleting')


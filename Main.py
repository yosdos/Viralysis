def Main():
     
    import pandas as pd
    from datetime import datetime
    import boto3
    
#******those are my function importation
#     %load XXXX.py
    from EnterancePerDay import EnterancePerDay 
    from DeleteItems import DeleteItems 
# ********************

    dynamodb = boto3.resource('dynamodb')
    Feed_table = dynamodb.Table('viralysisTable1')
    Data_table = dynamodb.Table('AllDataViralysis')

    Feed_tableS = Feed_table.scan()
    Feed_tableS.get('Items')
    Pandas_Feed_table = pd.DataFrame.from_dict(Feed_tableS.get('Items'))

#     Get the new feed and put them in the new table
    for i in Feed_tableS.get('Items'):
        Data_table.put_item(Item=i)
        
        
#   update the enterance table   
    EnterancePerDay(Pandas_Feed_table)   
    #delete feedTable
    DeleteItems('viralysisTable1')


Main()


def EnterancePerDay(Pandas_Feed_table):
    import pandas as pd
    from datetime import datetime
    import boto3
    print('Analizing...')
    
    '''
    Update the table with the number of 
    Enterance per day
    '''
    NameOFTable = 'NumberOfEnterance'
    dynamodb = boto3.resource('dynamodb')
    Enterance_Table = dynamodb.Table(NameOFTable)
    
    # PANDAS
    Pandas_Feed_table['dt_object'] = [datetime.fromtimestamp(float(i)).strftime("%m/%d/%Y") 
                                      for i in Pandas_Feed_table.time]
    
#     Pandas_Feed_table['Client'] = [json.loads(s.replace("'", "\""))['ViralysisClientId'] 
# #                                for s in Pandas_Feed_table['body-json']]

    groupbyTime = Pandas_Feed_table.groupby('dt_object').count().loc[:, ['body-json']]
    groupbyTime.reset_index(inplace=True)
    groupbyTime.columns=['Date','Num of enterance']
    #-------#
    groupbyTimeDict = groupbyTime.T.to_dict().values()
    print('Add data to {} table'.format(NameOFTable))
    #Update the Feature Table:
    for event in groupbyTimeDict:
        Enterance_Table.update_item(Key={'Date':event['Date']},
         AttributeUpdates={
            'Num of enterance': {
                'Value': event['Num of enterance'],
                'Action':'ADD'}})

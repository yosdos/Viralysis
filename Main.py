def Main():
     
    import pandas as pd
    from datetime import datetime
    import boto3

    from Add_Items_And_Delete_Items import Add_Items_And_Delete_Items

    from EnterancePerDay import EnterancePerDay 


    Pandas_Feed_table = Add_Items_And_Delete_Items()

    EnterancePerDay(Pandas_Feed_table) #Update the enterance table

    print('Done')

Main()

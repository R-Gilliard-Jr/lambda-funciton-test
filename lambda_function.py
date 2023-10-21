import pandas as pd
from datetime import date
import json

def lambda_handler(event, context):
    date_frame = pd.DataFrame([date.today()], columns = ["today"])
    date_frame = {'date' : date.today().strftime("%Y-%m-%d")}
    return {
        'statusCode': 200,
        'body': date_frame
    }
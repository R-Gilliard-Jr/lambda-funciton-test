import boto3

session = boto3.Session(profile_name = 'dev')
lambda_client = boto3.client('lambda')

response = lambda_client.invoke(
    FunctionName = "date_data_frame"
)
data = response['Payload'].read()
print(data)
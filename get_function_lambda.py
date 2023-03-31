import boto3, os
from botocore.config import Config
client = boto3.client('lambda')
# client = boto3.resource('s3', config=Config(proxies={'https': '10.134.151.10:8080'}))

response = client.list_functions(
    MasterRegion='string',
    FunctionVersion='ALL',
    Marker='string',
    MaxItems=123
)

print(response)
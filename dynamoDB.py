import json
import datetime
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('crawling')
client = boto3.client('dynamodb')

def handler(event, context):
    client.put_item(TableName='crawling',Item={'id':{'S':'행복해'}})
    return '완료'


def get_item():
    r = table.get_item(Key={'id': '친환경세제'})
    return r['Item']

import json
import os
import boto3
import uuid

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    data = json.loads(event['body'])
    print(data)

    project_name = data['project_name']

    # first_name_key = data['first_name']
    first_name_en = data['first_name']

    first_name_fr = data['Prénom']

    first_name_cn = data['名']


    # en_dict = {first_name_key: first_name_value}

    DBtable = os.environ['AppTable']

    if first_name_en and first_name_fr and first_name_cn:
        response = client.put_item(
            TableName=DBtable,
            Item={
                'id': {
                    'S': uuid.uuid4().hex
                },
                'first_name_en': {
                    'S': first_name_en
                },
                'first_name_fr': {
                    'S': first_name_fr
                },
                'first_name_cn': {
                    'S': first_name_cn
                },
            }
        )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }

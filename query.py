import boto3
from boto3.dynamodb.conditions import Key

def query_id(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1',aws_access_key_id='ASIA3ITFFU4NRIBNGQGX',
        aws_secret_access_key='C/QOKs+CXbyHlUXPnIvqjTqZqtanPeF4lCAqc94+',
        aws_session_token='FwoGZXIvYXdzEFcaDMJAvXum4v/F3Vrl3CLRAeuNXihAYgSvgqialbANwxPAwmoJFi+7Lr6ejtD66kGW9KdBkhQHbbS692/90yge95XzCcQ6HSmmxS5afaLH2KEmpDfuDg/7F7nTT5QaEJa/78YqeEz+g+IzfVYHcYSfF8m8zGi012+q14Q1fgzdlbo0d7U0Fc+fimoYrh+cbvxCmYpGTMOwzFEBch0zNaSa5VmIE9fB8D5kJIviP8zDkXmPHPCV8n2Kjezi3UMkgzQQGe0scbFxMYm2t1WmEiDoIWxCQH2tHpARn2rnTFjqSFAMKKD+rPoFMi2agZA1Z+s44/Mcg/e3LdtpC16IV7UP8eo6TPzBU7lkaU4sVs9+uwgqhoEgzn8=') 
    table = dynamodb.Table('details')
    scan_kwargs = {
        'ProjectionExpression': "#id, degree, university, percentage",
        'ExpressionAttributeNames': {"#id": "id"}
    }
    response = table.scan(**scan_kwargs)
    #response = table.query(KeyConditionExpression=Key('id').eq(year))
    #return response['Items']
    return response['Items']


def query_id2(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1',aws_access_key_id='ASIA3ITFFU4NRIBNGQGX',
        aws_secret_access_key='C/QOKs+CXbyHlUXPnIvqjTqZqtanPeF4lCAqc94+',
        aws_session_token='FwoGZXIvYXdzEFcaDMJAvXum4v/F3Vrl3CLRAeuNXihAYgSvgqialbANwxPAwmoJFi+7Lr6ejtD66kGW9KdBkhQHbbS692/90yge95XzCcQ6HSmmxS5afaLH2KEmpDfuDg/7F7nTT5QaEJa/78YqeEz+g+IzfVYHcYSfF8m8zGi012+q14Q1fgzdlbo0d7U0Fc+fimoYrh+cbvxCmYpGTMOwzFEBch0zNaSa5VmIE9fB8D5kJIviP8zDkXmPHPCV8n2Kjezi3UMkgzQQGe0scbFxMYm2t1WmEiDoIWxCQH2tHpARn2rnTFjqSFAMKKD+rPoFMi2agZA1Z+s44/Mcg/e3LdtpC16IV7UP8eo6TPzBU7lkaU4sVs9+uwgqhoEgzn8=') 
    table = dynamodb.Table('details')
    response = table.query(KeyConditionExpression=Key('id').eq(year))
    return response['Items']


# if __name__ == '__main__':
#     myid = '2'
#     print(f"Movies from {myid}")
#     results = query_id(myid)
#     for r in results:
#         print(r['degree'], ":", r['university'],":", r['percentage'])

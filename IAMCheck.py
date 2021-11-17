import boto3
from botocore.exceptions import ClientError

# Create IAM client
#iam = boto3.client('iam')

iam = boto3.resource('iam')
access_key_pair = iam.AccessKeyPair('user_name','id','secret')
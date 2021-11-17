# Verifying Public Access on S3 in Cloud Environment
import boto3
from botocore.exceptions import ClientError

#client = boto3.client('s3')

s3 = boto3.resource('s3')
print("---------------------------------------------------------------------------")
print("The following S3 buckets are in FULL_CONTROL permission. Please be alerted!")
print("---------------------------------------------------------------------------")
for bucket in s3.buckets.all():
    for s3_permission in s3.BucketAcl(bucket.name).grants:
        #result = client.get_bucket_acl(Bucket=bucket.name)
        pass
        #print(oh_noes)
        if s3_permission['Permission'] == 'FULL_CONTROL':
            # pass
            print(f"{bucket.name} :: {s3_permission}")

# Verifying users without MFA in Cloud Environment
client = boto3.client('iam')
iam_users = []
response = client.list_users()
for user in response['Users']:
    iam_users.append(user['UserName'])
while 'Marker' in response:
    response = client.list_users(Marker=response['Marker'])
    for user in response['Users']:
        iam_users.append(user['UserName'])

no_mfa_users = []
for iam_user in iam_users:
    response = client.list_mfa_devices(UserName=iam_user)
    if not response['MFADevices']:
        no_mfa_users.append(iam_user)




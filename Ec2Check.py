
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
print('Regions:', response['Regions'])

#Amazon EC2 key pairs
response_key_pairs = ec2.describe_key_pairs()
print(response_key_pairs)
# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()
#print('Availability Zones:', response['AvailabilityZones'])
print("---------------------------------------------------------------------------")
print("The following Security groups attached to EC2 instances can be accessed from any IP's. Please be alerted!")
print("---------------------------------------------------------------------------")
try:
    response = ec2.describe_security_groups()
    for securityGroups in response['SecurityGroups']:
        for IpPermissions in securityGroups["IpPermissions"]:
            for ipRAnges in IpPermissions["IpRanges"]:
                if ipRAnges['CidrIp'] == '0.0.0.0/0':
                    print(securityGroups)

    #print(response)

except ClientError as e:
    print(e)
import boto3

session = boto3.Session(
    				aws_access_key_id='X',
    				aws_secret_access_key='Y',
				)
ec2 = session.client('ec2', region_name='us-east-1')
response = ec2.create_snapshots(
    Description='snapshot--2',
    InstanceSpecification={
        'InstanceId': 'String',
        'ExcludeBootVolume': False
    }
)
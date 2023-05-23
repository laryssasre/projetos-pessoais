import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

tags = ['project', 'country', 'category', 'component', 'environment', 'venture', 'owner']

instances = ec2.describe_instances()

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        private_ip = instance['PrivateIpAddress']
        instance_tags = instance.get('Tags', [])
        missing_tags = [tag for tag in tags if tag not in [t['Key'] for t in instance_tags]]

        if missing_tags:
            print(f"Instância de ID {instance_id} e PrivateIp {private_ip} não possui as seguintes tags: {', '.join(missing_tags)}")
        else:
            print(f"Instância de ID {instance_id} e PrivateIp {private_ip} possui todas as tags da planilha.")

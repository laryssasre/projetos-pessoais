import csv
import boto3


file_path = '/path/to/file/file.csv'

ec2 = boto3.client('ec2', region_name='us-east-1')

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        instance_id = row['instance_id']
        project = row['project']
        country = row['country']
        category = row['category']
        component = row['component']
        environment = row['environment']
        venture = row['venture']
        owner = row['owner']

        response = ec2.describe_instances(InstanceIds=[instance_id])

if response['Reservations']:
    ec2.create_tags(Resources=[instance_id], Tags=[
        {'Key': 'project', 'Value': row['project']},
        {'Key': 'country', 'Value': row['country']},
        {'Key': 'category', 'Value': row['category']},
        {'Key': 'component', 'Value': row['component']},
        {'Key': 'environment', 'Value': row['environment']},
        {'Key': 'venture', 'Value': row['venture']},
        {'Key': 'owner', 'Value': row['owner']}
    ])
    print("Tags criadas com sucesso!")
else:
    print(f"Não foi possível encontrar uma instância com o ID {instance_id}.")

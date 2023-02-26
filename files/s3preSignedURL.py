import boto3

url = boto3.client('s3').generate_presigned_url(
        ClientMethod='get_object', 
        Params={'Bucket': 'iso-693051501776', 'Key': 'iso/vmware/VMware-VCSA-all-6.7.0-18485166.iso'},
        ExpiresIn=3600)
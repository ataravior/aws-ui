import boto3
from fastapi import HTTPException

route53 = boto3.client("route53")

def create_hosted_zone(domain_name: str):
    """ יוצר Hosted Zone חדש ב-Route 53 """
    try:
        response = route53.create_hosted_zone(
            Name=domain_name,
            CallerReference=domain_name,
            HostedZoneConfig={"Comment": "Created via API", "PrivateZone": False}
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

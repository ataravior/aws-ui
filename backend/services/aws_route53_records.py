# services/route53_records_service.py
import boto3
from fastapi import HTTPException

route53 = boto3.client("route53")

def create_dns_record(zone_id: str, record_name: str, record_type: str, record_value: str):
    """ יוצר רשומת DNS ב-Route 53 """
    try:
        response = route53.change_resource_record_sets(
            HostedZoneId=zone_id,
            ChangeBatch={
                "Changes": [
                    {
                        "Action": "CREATE",
                        "ResourceRecordSet": {
                            "Name": record_name,
                            "Type": record_type,
                            "TTL": 300,
                            "ResourceRecords": [{"Value": record_value}]
                        }
                    }
                ]
            }
        )
        return {"message": f"DNS Record '{record_name}' ({record_type}) created successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def list_dns_records(zone_id: str):
    """ מחזיר את כל הרשומות ב-Route 53 עבור Zone מסוים """
    try:
        response = route53.list_resource_record_sets(HostedZoneId=zone_id)
        records = [
            {"name": r["Name"], "type": r["Type"], "values": [v["Value"] for v in r.get("ResourceRecords", [])]}
            for r in response["ResourceRecordSets"]
        ]
        return {"records": records}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def delete_dns_record(zone_id: str, record_name: str, record_type: str):
    """ מוחק רשומת DNS ב-Route 53 """
    try:
        response = route53.change_resource_record_sets(
            HostedZoneId=zone_id,
            ChangeBatch={
                "Changes": [
                    {
                        "Action": "DELETE",
                        "ResourceRecordSet": {
                            "Name": record_name,
                            "Type": record_type,
                            "TTL": 300,
                            "ResourceRecords": [{"Value": "DELETE"}]
                        }
                    }
                ]
            }
        )
        return {"message": f"DNS Record '{record_name}' deleted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

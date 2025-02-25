from fastapi import APIRouter
from backend.services.aws_route53 import Route53Service
router = APIRouter(prefix="/route53", tags=["Route 53"])

# 🎯 Hosted Zones
@router.get("/zones")
async def get_hosted_zones():
    """ מחזיר רשימת Hosted Zones """
    return Route53Service.list_hosted_zones()

@router.post("/zones")
async def post_hosted_zone(domain_name: str):
    """ יוצר Hosted Zone חדש """
    return Route53Service.create_hosted_zone(domain_name)

@router.delete("/zones/{zone_id}")
async def remove_hosted_zone(zone_id: str):
    """ מוחק Hosted Zone """
    return Route53Service.delete_hosted_zone(zone_id)

# 🎯 רשומות DNS
@router.get("/records/{zone_id}")
async def get_dns_records(zone_id: str):
    """ מחזיר את כל הרשומות של Hosted Zone """
    return Route53Service.list_dns_records(zone_id)

@router.post("/records")
async def post_dns_record(zone_id: str, record_name: str, record_type: str, record_value: str):
    """ יוצר רשומת DNS חדשה """
    return Route53Service.create_dns_record(zone_id, record_name, record_type, record_value)

@router.delete("/records")
async def remove_dns_record(zone_id: str, record_name: str):
    """ מוחק רשומת DNS """
    return Route53Service.delete_dns_record(zone_id, record_name)

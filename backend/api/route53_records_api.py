# api/route53_records_api.py
from fastapi import APIRouter
from backend.services.aws_route53_records import create_dns_record, list_dns_records, delete_dns_record

router = APIRouter(prefix="/route53/records", tags=["Route53 Records"])

@router.post("/create")
async def create_record(zone_id: str, record_name: str, record_type: str, record_value: str):
    return create_dns_record(zone_id, record_name, record_type, record_value)

@router.get("/list")
async def list_records(zone_id: str):
    return list_dns_records(zone_id)

@router.delete("/delete")
async def delete_record(zone_id: str, record_name: str, record_type: str):
    return delete_dns_record(zone_id, record_name, record_type)

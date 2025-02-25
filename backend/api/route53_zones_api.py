# from fastapi import APIRouter
# from backend.services.aws_route53_zones import create_hosted_zone, list_hosted_zones, delete_hosted_zone

# router = APIRouter(prefix="/route53/zones", tags=["Route53 Zones"])

# @router.post("/create")
# def create_zone(domain_name: str):
#     """Creates a hosted zone"""
#     return create_hosted_zone(domain_name)

# @router.get("/list")
# def list_zones():
#     """Lists all hosted zones"""
#     return list_hosted_zones()

# @router.delete("/delete/{zone_id}")
# def delete_zone(zone_id: str):
#     """Deletes a hosted zone"""
#     return delete_hosted_zone(zone_id)

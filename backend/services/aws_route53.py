from fastapi import HTTPException
import backend.services.aws_route53_zones as aws_route53_zones
import backend.services.aws_route53_records as aws_route53_records

class Route53Service:
    @staticmethod
    def list_hosted_zones():
        """ מחזיר את כל ה-Hosted Zones ב-Route 53 """
        try:
            return aws_route53_zones.list_hosted_zones()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_hosted_zone(domain_name: str):
        """ יוצר Hosted Zone חדש """
        try:
            return aws_route53_zones.create_hosted_zone(domain_name)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_hosted_zone(zone_id: str):
        """ מוחק Hosted Zone """
        try:
            return aws_route53_zones.delete_hosted_zone(zone_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def list_dns_records(zone_id: str):
        """ מחזיר את כל הרשומות ב-Route 53 עבור Hosted Zone """
        try:
            return aws_route53_records.list_dns_records(zone_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_dns_record(zone_id: str, record_name: str, record_type: str, record_value: str):
        """ יוצר רשומת DNS חדשה """
        try:
            return aws_route53_records.create_dns_record(zone_id, record_name, record_type, record_value)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_dns_record(zone_id: str, record_name: str):
        """ מוחק רשומת DNS """
        try:
            return aws_route53_records.delete_dns_record(zone_id, record_name)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

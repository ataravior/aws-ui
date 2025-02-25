import boto3
from fastapi import HTTPException

s3 = boto3.client("s3")

class S3Service:
    @staticmethod
    def list_s3_buckets():
        """מחזיר רשימה של דליים (Buckets) ב-S3"""
        response = s3.list_buckets()
        buckets = []

        for bucket in response["Buckets"]:
            bucket_name = bucket["Name"]
            try:
                tags_response = s3.get_bucket_tagging(Bucket=bucket_name)
                tags = {tag["Key"]: tag["Value"] for tag in tags_response["TagSet"]}
                if tags.get("CreatedBy") == "Pulumi" or "Owner" in tags:
                    buckets.append({"bucket_name": bucket_name, "owner": tags.get("Owner", "N/A")})
            except s3.exceptions.ClientError:
                pass

        return {"buckets": buckets} if buckets else {"message": "No S3 buckets found."}

    @staticmethod
    def upload_file_to_s3(bucket_name: str, file_path: str):
        """מעלה קובץ לדלי S3"""
        try:
            s3.upload_file(file_path, bucket_name, file_path.split("/")[-1])
            return {"message": f"File '{file_path}' uploaded to '{bucket_name}' successfully."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_s3_bucket(bucket_name: str):
        """מוחק דלי S3"""
        try:
            s3.delete_bucket(Bucket=bucket_name)
            return {"message": f"S3 bucket '{bucket_name}' deleted successfully."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_s3_bucket(bucket_name: str, bucket_type: str):
        """יוצר דלי S3 עם תגיות"""
        try:
            s3.create_bucket(Bucket=bucket_name)
            s3.put_bucket_tagging(
                Bucket=bucket_name,
                Tagging={"TagSet": [{"Key": "Owner", "Value": "avioratar"}, {"Key": "CreatedBy", "Value": "Pulumi"}]}
            )
            return {"message": f"S3 bucket '{bucket_name}' created successfully."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter, UploadFile, File
from backend.services.aws_s3 import S3Service
router = APIRouter(prefix="/s3", tags=["S3"])

@router.get("/list")
async def list_buckets():
    """מחזיר רשימת דליים (Buckets) ב-S3"""
    return S3Service.list_s3_buckets()

@router.post("/create")
async def create_bucket(bucket_name: str, bucket_type: str):
    """יוצר דלי S3"""
    return S3Service.create_s3_bucket(bucket_name, bucket_type)

@router.post("/upload")
async def upload_file(bucket_name: str, file: UploadFile = File(...)):
    """מעלה קובץ לדלי S3"""
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    
    return S3Service.upload_file_to_s3(bucket_name, file_location)

@router.delete("/delete")
async def delete_bucket(bucket_name: str):
    """מוחק דלי S3"""
    return S3Service.delete_s3_bucket(bucket_name)

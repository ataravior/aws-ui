from fastapi import APIRouter
from backend.services.ec2_service import EC2Service
from pydantic import BaseModel

# יצירת ראוטר לניהול API של EC2
router = APIRouter(prefix="/ec2", tags=["EC2"])

class CreateInstanceRequest(BaseModel):
    instance_name: str
    instance_type: str
    ami: str
    pubkey_path: str

@router.get("/list")
def list_instances():
    """ מחזיר את רשימת מופעי EC2 """
    return EC2Service.list_instances()

@router.post("/create")
def create_instance(request: CreateInstanceRequest):
    """ יוצר מופע EC2 חדש """
    return EC2Service.create_instance(
        instance_name=request.instance_name,
        instance_type=request.instance_type,
        ami=request.ami,
        pubkey_path=request.pubkey_path
    )

@router.post("/start/{instance_id}")
def start_instance(instance_id: str):
    """מתחיל מופע EC2"""
    return EC2Service.start_instance(instance_id)

@router.post("/stop/{instance_id}")
def stop_instance(instance_id: str):
    """עוצר מופע EC2"""
    return EC2Service.stop_instance(instance_id)
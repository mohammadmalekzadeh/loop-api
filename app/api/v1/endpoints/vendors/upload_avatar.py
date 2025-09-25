from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.config import BUCKET_ACCESS_KEY, BUCKET_ENDPOINT_URL, BUCKET_NAME, BUCKET_SECRET_KEY
from app.models.vendors import Vendors
from app.deps.current_user import get_db, get_current_user
import boto3
import uuid

router = APIRouter(prefix="/upload-avatar", tags=["Upload Avatar"])

s3_client = boto3.client(
    "s3",
    aws_access_key_id=BUCKET_ACCESS_KEY,
    aws_secret_access_key=BUCKET_SECRET_KEY,
    endpoint_url=BUCKET_ENDPOINT_URL
)

@router.post("/upload", summary="Upload image for vendors avatar")
async def upload(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: Session = Depends(get_current_user)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="image format is wrong, just png or jpg")
    
    ext = file.filename.split(".")[-1]
    file_key = f"uploads/{uuid.uuid4()}.{ext}"

    try:
        s3_client.upload_fileobj(file.file, BUCKET_NAME, file_key)
        file_url = f"{BUCKET_ENDPOINT_URL}/{BUCKET_NAME}/{file_key}"

        vendors = db.query(Vendors).filter(Vendors.user_id == current_user.id).first()
        if not vendors:
            raise HTTPException(status_code=404, detail="Vendor not found")
        
        vendors.profile_image = file_url

        db.commit()
        db.refresh(vendors)

        return {"id": vendors.id, "url": vendors.profile_image}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))








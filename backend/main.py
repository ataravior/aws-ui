import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn

# יצירת אפליקציה ראשית
app = FastAPI(title="SkyOps API", description="API for managing AWS resources", version="1.0")

# הגדרת CORS Middleware
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# חיבור הפרונטאנד
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")


@app.get("/")
async def read_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))

# ייבוא API Routers
from backend.api.ec2_api import router as ec2_router
from backend.api.s3_api import router as s3_router
from backend.api.route53_api import router as route53_router
# from backend.api.route53_zones_api import router as route53_zones_router
from backend.api.route53_records_api import router as route53_records_router

# חיבור הנתיבים לאפליקציה
app.include_router(ec2_router, prefix="/api")
app.include_router(s3_router, prefix="/api")
app.include_router(route53_router, prefix="/api")
# app.include_router(route53_zones_router, prefix="/api/route53/zones")
app.include_router(route53_records_router, prefix="/api/route53")

# הרצת השרת
if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)

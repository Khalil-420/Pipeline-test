from fastapi import APIRouter, HTTPException
import requests
from models.task import TaskIn
import db.database as database
from services.syncthing_service import add_device_to_syncthing, add_folder_to_syncthing
from core.email import *

router = APIRouter()

@router.post("/api/task")
def create_task(task: TaskIn):
    try:
        add_device_to_syncthing(task.device_id, task.device_name)
        
        database.add_task(task.device_id, task.label, task.local_path, task.device_name, task.remote_path)
        
        # Add the remote folder to Syncthing
        # label is the folder you want to share
        add_folder_to_syncthing(task.remote_path, task.label, task.local_path, task.device_id)
        
        return {"message": "Task created, device and folders added to Syncthing"}
    except Exception as e:
        #send_email("Failed to Create Task", f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to create task: {e}")

@router.get("/api/task")
def get_all_tasks():
    tasks = database.get_all_tasks()
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")
    return tasks

@router.get("/api/device/stats")
def get_device_stats():
    url = f"{settings.SYNCTHING_URL}/rest/stats/device"
    headers = {"X-API-Key": settings.SYNCTHING_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve device stats")
    return response.json()

@router.get("/api/folder/stats")
def get_folder_stats():
    url = f"{settings.SYNCTHING_URL}/rest/stats/folder"
    headers = {"X-API-Key": settings.SYNCTHING_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve folder stats")
    return response.json()


@router.get("/api/status")
def check_syncthing_status():
    url = f"{settings.SYNCTHING_URL}/rest/noauth/health"
    headers = {"X-API-Key": settings.SYNCTHING_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve Syncthing status")
    return response.json()

@router.get("/api/test-email")
def test_email():
    try:
        send_email("Test Email", settings.EMAIL_TO,"This is a test email from FastAPI microservice.")
        return {"message": "Test email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send test email")


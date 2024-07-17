import requests
from fastapi import HTTPException
from core.config import settings
from core.email import send_email

def check_syncthing_status(x: int = None):
    url = f"{settings.SYNCTHING_URL}/rest/noauth/health"
    headers = {"X-API-Key": settings.SYNCTHING_API_KEY}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if x==1:
            send_email("Syncthing Service UP", settings.EMAIL_TO,f"Syncthing is UP.")
        return True
    except:
        if x==0:
           send_email("Syncthing Service Down", settings.EMAIL_TO,f"Syncthing is down.")
        return False

def add_device_to_syncthing(device_id: str, device_name: str):
    url = f"{settings.SYNCTHING_URL}/rest/config/devices"
    headers = {"X-API-Key": settings.SYNCTHING_API_KEY}
    
    new_device = {
        "deviceID": device_id,
        "name": device_name,
        "addresses": ["dynamic"],
        "compression": "metadata"
    }
    
    response = requests.post(url, json=new_device, headers=headers)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to add new device to Syncthing")

def add_folder_to_syncthing(remote_path: str, label: str, path: str, device_id: str ):
    url = f"{settings.SYNCTHING_URL}/rest/config/folders"
    headers = {"X-API-Key": settings.SYNCTHING_API_KEY}
    
    new_folder = {
        "id": remote_path,
        "label": label,
        "path": path,
        "devices": [
            {"deviceID": settings.LOCAL_DEVICE_ID},
            {"deviceID": device_id}
        ]
    }
    
    
    response = requests.post(url, json=new_folder, headers=headers)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to add new folder to Syncthing")
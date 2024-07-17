from pydantic import BaseModel

class TaskIn(BaseModel):
    device_id: str
    device_name: str
    label: str
    local_path: str
    remote_path: str

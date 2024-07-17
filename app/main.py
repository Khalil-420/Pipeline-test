import asyncio
from fastapi import FastAPI
from api.routes import router as api_router
from services.syncthing_service import check_syncthing_status
from db.database import initialize_database

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    initialize_database()
    asyncio.create_task(monitor_syncthing())


async def monitor_syncthing():    
    z=0   # To send mail one time per status
    while True:
        mail_sent = check_syncthing_status(z)
        if mail_sent == False:
            z=1
        elif mail_sent == True and z==1:
            z=0
        await asyncio.sleep(1)  # Check every 10 minutes

app.include_router(api_router)
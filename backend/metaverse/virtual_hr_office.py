import pytorch3d
from fastapi import FastAPI

class VirtualHROffice:
    def __init__(self):
        self.environment = "3D AI HR Office"

    def welcome_employee(self, name):
        return f"👋 Welcome to your AI-powered Virtual HR Office, {name}!"

app = FastAPI()
virtual_hr = VirtualHROffice()

@app.get("/virtual_office")
async def enter_office(name: str):
    return virtual_hr.welcome_employee(name)
from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from random import uniform  # ✅ Import this for random sensor values

app = FastAPI()

# Ensure 'static' directory exists
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],  # Only allow frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Dummy User Database
users_db = {
    "admin": "password123",
    "user": "test123",
    "maha": "password123"
}

user_sessions = {}  # Authentication token storage

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# 🔹 Request Models
class LoginRequest(BaseModel):
    username: str
    password: str

class FaultDetectionRequest(BaseModel):
    machine_id: str
    temperature: Optional[float] = None
    vibration: Optional[float] = None
    pressure: Optional[float] = None

# 🔹 Login API
@app.post("/login")
async def login(user: LoginRequest):
    if user.username in users_db and users_db[user.username] == user.password:
        token = f"token_{user.username}"
        user_sessions[token] = user.username
        return {"message": "Login successful", "token": token}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")

# 🔹 Middleware for Authentication
def get_current_user(token: str = Depends(oauth2_scheme)):
    if token not in user_sessions:
        raise HTTPException(status_code=401, detail="Not authenticated. Please log in.")
    return user_sessions[token]

# 🔹 ✅ UPDATED: Fault Detection API with Random Values
@app.post("/fault-detection")
async def detect_fault(request: FaultDetectionRequest, current_user: str = Depends(get_current_user)):
    # Simulate real-time sensor readings (if real data is unavailable)
    temperature = request.temperature if request.temperature is not None else round(uniform(50, 100), 2)
    vibration = request.vibration if request.vibration is not None else round(uniform(2, 8), 2)
    pressure = request.pressure if request.pressure is not None else round(uniform(80, 140), 2)

    fault_detected = None
    confidence = 100
    suggested_action = "System Stable"

    if temperature > 70:
        fault_detected = "Overheating"
        confidence = 92
        suggested_action = "Reduce Load"

    if vibration > 5:
        fault_detected = "Excessive Vibration"
        confidence = 85
        suggested_action = "Inspect Bearings"

    if pressure > 120:
        fault_detected = "High Pressure"
        confidence = 88
        suggested_action = "Check Valves"

    response = {
        "machine_id": request.machine_id,
        "fault_detected": fault_detected if fault_detected else "No Faults Detected",
        "temperature": temperature,
        "vibration": vibration,
        "pressure": pressure,
        "confidence": confidence,
        "suggested_action": suggested_action
    }

    if fault_detected:
        notify_user(request.machine_id, fault_detected, temperature, vibration, pressure)

    return response

# 🔹 Dashboard API
@app.get("/dashboard")
async def dashboard(current_user: str = Depends(get_current_user)):
    return {"message": f"Welcome to the dashboard, {current_user}!"}

# 🔹 Root Endpoint
@app.get("/")
def read_root():
    return {"message": "AI-Driven Fault Detection API is Running"}

import smtplib
from fastapi import APIRouter, HTTPException
from twilio.rest import Client
from pydantic import BaseModel

router = APIRouter()

# Dummy user database
users_db = {
    "admin": "password123",
    "user": "test123",
    "maha": "password123"
}

# Email Configurations
EMAIL_SENDER = "your-email@gmail.com"  # 🔹 Replace with your email
EMAIL_PASSWORD = "your-email-password"  # 🔹 Replace with your app password (for Gmail, use App Password)
EMAIL_RECEIVER = "receiver-email@example.com"  # 🔹 Replace with recipient's email
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Twilio Configurations
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"  # 🔹 Your Twilio number
USER_PHONE_NUMBER = "+0987654321"  # 🔹 Recipient's phone number

# Login Request Model
class LoginRequest(BaseModel):
    username: str
    password: str

# Email Sending Function
def send_email(subject, body):
    print(f"📨 Sending email to {EMAIL_RECEIVER}...\nSubject: {subject}\nBody: {body}")
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, f"Subject: {subject}\n\n{body}")
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")

# SMS Sending Function
def send_sms(message):
    print(f"📱 Sending SMS to {USER_PHONE_NUMBER}...\nMessage: {message}")
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=USER_PHONE_NUMBER
        )
        print("✅ SMS sent successfully!")
    except Exception as e:
        print(f"❌ SMS sending failed: {e}")

# Fault Detection API Endpoint
@router.post("/detect_fault")
async def detect_fault():
    fault_message = "⚠️ Fault detected in the machine! Immediate action required."
    
    # Send Email and SMS Alerts
    send_email("Fault Alert", fault_message)
    send_sms(fault_message)
    
    return {"message": "Fault detected and notifications sent!"}
import smtplib
from fastapi import APIRouter, HTTPException
from twilio.rest import Client
from pydantic import BaseModel

router = APIRouter()

# Dummy user database
users_db = {
    "admin": "password123",
    "user": "test123",
    "maha": "password123"
}

# Email Configurations
EMAIL_SENDER = "your-email@gmail.com"  # 🔹 Replace with your email
EMAIL_PASSWORD = "your-email-password"  # 🔹 Replace with your app password (for Gmail, use App Password)
EMAIL_RECEIVER = "receiver-email@example.com"  # 🔹 Replace with recipient's email
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Twilio Configurations
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"  # 🔹 Your Twilio number
USER_PHONE_NUMBER = "+0987654321"  # 🔹 Recipient's phone number

# Login Request Model
class LoginRequest(BaseModel):
    username: str
    password: str

# Email Sending Function
def send_email(subject, body):
    print(f"📨 Sending email to {EMAIL_RECEIVER}...\nSubject: {subject}\nBody: {body}")
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, f"Subject: {subject}\n\n{body}")
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")

# SMS Sending Function
def send_sms(message):
    print(f"📱 Sending SMS to {USER_PHONE_NUMBER}...\nMessage: {message}")
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=USER_PHONE_NUMBER
        )
        print("✅ SMS sent successfully!")
    except Exception as e:
        print(f"❌ SMS sending failed: {e}")

# Fault Detection API Endpoint
@router.post("/detect_fault")
async def detect_fault():
    fault_message = "⚠️ Fault detected in the machine! Immediate action required."
    
    # Send Email and SMS Alerts
    send_email("Fault Alert", fault_message)
    send_sms(fault_message)
    
    return {"message": "Fault detected and notifications sent!"}

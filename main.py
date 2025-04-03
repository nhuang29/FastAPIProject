from fastapi import FastAPI, Form, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List

DATABASE_URL = "sqlite:///./lead.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model
class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    resume = Column(String, unique=True, index=True)
    status = Column(String, unique=False, index=True)

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

# Pydantic schema
from pydantic import BaseModel

class LeadCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    resume: str

class LeadUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str

class LeadResponse(LeadCreate):
    id: int
    status: str
    class Config:
        from_attributes = True

# Credentials for log in
USERNAME="admin"
PASSWORD="admin"

# Method to submit application
@app.post("/leads/", response_model=LeadResponse)
def create_user(lead: LeadCreate, db: Session = Depends(get_db)):
    try:
        lead_db = Lead(first_name=lead.first_name, last_name=lead.last_name, email=lead.email, resume=lead.resume,
                       status="pending")
        db.add(lead_db)
        db.commit()
        db.refresh(lead_db)
        return lead_db
    except Exception as e:
        return {"Message": str(e)}


# Method to get a specific lead applicant
@app.get("/leads/{lead_id}", response_model=LeadResponse)
def get_lead(lead_id: int, db: Session = Depends(get_db)):
    try:
        lead = db.query(Lead).filter(Lead.id == lead_id).first()
        if not lead:
            raise HTTPException(status_code=404, detail="User not found")
        return lead
    except Exception as e:
        return {"Message": str(e)}


# Method to get all lead applicants
@app.get("/leads/", response_model=List[LeadResponse])
def get_all_leads(db: Session = Depends(get_db)):
    try:
        leads = db.query(Lead).all()
        if not leads:
            raise HTTPException(status_code=404, detail="Lead Database is empty")
        return leads
    except Exception as e:
        return {"Message": str(e)}


# Method to change the status of the applicant if reached out to
@app.put("/leads/", response_model=LeadResponse)
def change_lead_status(lead: LeadUpdate, db: Session = Depends(get_db)):
    try:
        lead = db.query(Lead).filter(Lead.first_name == lead.first_name
                                     and Lead.last_name == lead.last_name
                                     and Lead.email == lead.email).first()

        if not lead:
            raise HTTPException(status_code=404, detail="Lead not found")

        if lead.status == "reached out":
            return lead
        else:
            lead.status = "reached out"
            db.commit()
            db.refresh(lead)
            return lead
    except Exception as e:
        return {"Message": str(e)}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == USERNAME and password == PASSWORD:
        return templates.TemplateResponse("index.html", {"request": request, "username": username})
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    # Simulate clearing the session
    return RedirectResponse(url="/")




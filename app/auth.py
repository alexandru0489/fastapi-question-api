from fastapi import HTTPException, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
from .database import SessionLocal
from .models import User

security = HTTPBasic()


users = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine",
    "admin": "4dm1N"
}


def get_current_user(credentials: HTTPBasicCredentials = Security(security)):
    db = SessionLocal()
    user = db.query(User).filter(User.username == credentials.username).first()
    db.close()
    if user is None or user.password != credentials.password:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"}
        )    
    return user.username
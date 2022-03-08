from datetime import datetime, timedelta
from typing import Optional, Dict

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.models import User
from app import schemas
from app.core.config import config
from app.api.dependencies import get_database

"""
file holds all of the important methods/ endpoints for validating a user
this includes creating a user in the database when they register
and looking for users on login
"""

router = APIRouter()

pwd_context = CryptContext(schemes=['sha256_crypt'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

denylist: set = set()


def get_password_hash(password: str) -> bytes:
    """function to generate a password hash given a plaintext password"""
    return pwd_context.hash(password)

def verify_password(plaintext, hash) -> bool:
    """function to verify that the given plaintext password matches the hash"""
    return pwd_context.verify(plaintext, hash)

def authenticate_user(database, username: str, password: str) -> Optional[User]:
    """function to check the validity of the given user"""
    user = database.query(User).where(username == User.username).first()

    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    """creates an access token for the given user with a default timeout of 15 minutes"""

    expire = datetime.utcnow() + expires_delta
    return jwt.encode(data.copy() | {'exp' : expire}, config.SECRET_KEY, algorithm=config.ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme), database = Depends(get_database)) -> User:
    """function to get the current user given a jwt token"""
    credentials_exception = HTTPException(401, detail='could not validate credentials', headers={'WWW-Authenticate': 'Bearer'})
    if token in denylist:
        raise HTTPException(401, detail='invalid token', headers={'WWW-Authenticate': 'Bearer'})
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = database.query(User).where(username == User.username).first()
    if user is None:
        raise credentials_exception
    return user

@router.post('/login')
def login(database=Depends(get_database), form_data: OAuth2PasswordRequestForm = Depends()) -> Dict[str, str]:
    """endpoint to authenticate the given user"""
    user = authenticate_user(database, form_data.username, form_data.password)
    if not user:
        raise HTTPException(401, detail='incorrect username or password', headers={'WWW-Authenticate': 'Bearer'})
    token = create_access_token(data={'sub': user.username})
    return {'access_token': token, 'token_type': 'Bearer'}

@router.post('/logout')
def logout(token=Depends(oauth2_scheme)):
    """function to invalidate token"""
    denylist.add(token)

@router.put('/register', status_code=201)
def register(user: schemas.User, database = Depends(get_database)):
    """function to create a user"""
    pwd: str = get_password_hash(user.password)
    user_model: User = User(username=user.username, password=pwd)
    database.add(user_model)
    database.commit()

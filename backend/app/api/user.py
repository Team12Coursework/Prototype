from fastapi import APIRouter

router = APIRouter()

@router.post('/login')
def login():
    return {'msg': 'working'}

@router.post('/logout')
def logout():
    return {'msg': 'working'}

@router.post('/register')
def register():
    return {'msg': 'working'}
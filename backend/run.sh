export $(cat .env | xargs)
python3 -m uvicorn main:app --reload
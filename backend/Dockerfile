FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# install all of the project dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

# run the backend application through uvicorn, accepting any hosts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

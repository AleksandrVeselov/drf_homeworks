FROM python:3

WORKDIR /code

COPY ./requirement.txt /code/

RUN pip install -r requirements.txt

COPY . .


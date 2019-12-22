FROM python:3.6.8

EXPOSE 9001

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt


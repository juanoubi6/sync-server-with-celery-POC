FROM python:3.6.8

EXPOSE 9001

ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt

COPY . .

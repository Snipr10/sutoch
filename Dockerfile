FROM python:3.10-slim
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN pip3 install torch==1.8.1

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/
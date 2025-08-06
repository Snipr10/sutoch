FROM python:3.10-slim
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN pip3 install torch==1.8.1

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN python -m ensurepip --upgrade && python -m pip install --upgrade pip --no-progress-bar
RUN pip3 install -r requirements.txt

# copy project
COPY . /usr/src/app/
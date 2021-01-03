FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY '!&s2&ceggpl8beo$oflrhtn=o-20)=nb00p$8*7n$y@$#h_ud5'
ENV DEV False
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
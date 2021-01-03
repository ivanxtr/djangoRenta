FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY '!&s2&ceggpl8beo$oflrhtn=o-20)=nb00p$8*7n$y@$#h_ud5'
ENV DEV False
ENV NAME 'mzyttqnm82eu6d5z'
ENV USER 'njzcprcc1v9ce8q1'
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
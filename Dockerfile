FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY '!&s2&ceggpl8beo$oflrhtn=o-20)=nb00p$8*7n$y@$#h_ud5'
ENV DEV True
ENV NAME 'zurdnas69vi3mngr'
ENV USER 'njzcprcc1v9ce8q1'
ENV PASSWORD: 'mzyttqnm82eu6d5z'
ENV HOST: 'dt3bgg3gu6nqye5f.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
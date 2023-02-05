FROM python:3.11-slim-buster

WORKDIR /app

# System dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql libpq-dev \
    && apt-get clean

# Application dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app
COPY requirements-dev.txt /app
RUN pip install -r requirements-dev.txt

# Add app
COPY . /app

EXPOSE 8000

CMD ["python", "main.py"]

# Add entrypoint.sh 'Later'
#COPY ./entrypoint.sh /usr/src/
#RUN chmod +x /usr/src/entrypoint.sh
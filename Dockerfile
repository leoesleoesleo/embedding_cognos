FROM python:3.10.6-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependencies
RUN apt-get update && \
    apt-get install -y iputils-ping \
    && apt-get install -y default-libmysqlclient-dev build-essential \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir /app_cognos 
WORKDIR /app_cognos

COPY requirements/requirements.txt /app_cognos/
RUN pip install --upgrade pip==23.0.1

RUN pip install -r requirements.txt

EXPOSE 5005

# Run it
COPY . /app_cognos/

CMD ["python3", "main3.py"]

FROM python:3.11.0-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get -y install default-libmysqlclient-dev python3-dev gcc libc-dev mariadb-dev build-base

WORKDIR /app
COPY . /app

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/requirements.txt


# docker build -t django_image .
# docker build -t django_image -f Dockerfile .
# docker run -p 8001:8000 --name django_container -d django_image
# docker exec -it django_container python3 manage.py makemigrations
# docker exec -it django_container python3 manage.py migrate

# docker rmi django_image
# docker image rm django_image
# docker ps
# docker container ls

# docker run --name p8_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=1 -d -p 5432:5432 postgres:alpine
# docker exec -it -u postgres p8_db psql


# docker-compose -f docker-compose.yml build
# docker-compose build .
# docker-compose build --no-cache
# docker-compose up
# docker-compose down -v
# docker-compose down

# dockerfile, docker-compose,docker-swarm


#https://www.dotnetthailand.com/web-frameworks/django/docker-compose-for-django-mysql
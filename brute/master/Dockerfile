# syntax=docker/dockerfile:1
FROM python:3
RUN pip install celery
RUN pip install cryptography
CMD celery --workdir /celery -A tasks worker -Q masterTasksQ --loglevel=INFO

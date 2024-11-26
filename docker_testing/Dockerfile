# EACH COMMAND CREATES A NEW IMAGE LAYER

# Use latest Python runtime as base image
FROM python:3.6.5-alpine3.7

# Set the working directory to /app and copy current dir
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir pytest

ENV PYTHONPATH=/app/src

# Run hello_world.py when the container launches
CMD ["pytest", "test/"]

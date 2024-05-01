# Use the official Python image as a base image
FROM python:3.8

# Set environment variables for Python and output buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

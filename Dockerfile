# Use an official Python runtime as a parent image
FROM python:3.8-slim
# Updating the repo and install ping command
RUN apt-get update -y && apt-get install iputils-ping -y
# Set the working directory in the container
RUN mkdir -p /app

WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
RUN cd /app
# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt
CMD ["streamlit","run","--server.port","8080","streamlit_main.py"]

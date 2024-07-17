# Syncthing Microservice

This project is a microservice built using FastAPI and Syncthing to manage and monitor backups of remote servers to a local machine. It also includes functionality to send email notifications if the Syncthing service is down.

## Features

- Add new remote devices and folders to Syncthing for synchronization
- Monitor the status of the Syncthing service and send email notifications if it goes down
- Manage tasks in an SQLite database
- Expose endpoints to interact with the service

## Setup

Setup syncthing in both remote and local : 

  Install syncthing : 
    sudo apt install syncthing

  Start and enable syncthing : 
    sudo systemctl start syncthing@$(whoami).service
    sudo systemctl enable syncthing@$(whoami).service

## Environment Variables

Ensure the following environment variables are set in your `docker-compose.yml` file:

```yaml
services:
  fastapi:
    environment:
      SYNCTHING_API_KEY: "your_syncthing_api_key"
      SYNCTHING_URL: "http://127.0.0.1:8384"
      LOCAL_DEVICE_ID: "your_local_device_id"
      EMAIL_HOST: "smtp.gmail.com"
      EMAIL_PORT: 587
      EMAIL_HOST_USER: "your_email@gmail.com"
      EMAIL_HOST_PASSWORD: "your_email_password"
      EMAIL_FROM: "your_email@gmail.com"
      EMAIL_TO: "recipient_email@gmail.com"




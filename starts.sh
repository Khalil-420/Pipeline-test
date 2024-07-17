#!/bin/sh

# Start cron service
service cron start

# Start uvicorn server
uvicorn app.main:app --host 0.0.0.0 --port 8000

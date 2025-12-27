# Dockerized Flask To-Do App



## Description

A minimal To-Do list application built with Python Flask and Docker.  

Includes a simple browser UI to add tasks, view tasks, and mark tasks as done.



## Step 1: Docker Installation on Linux

```bash

sudo apt update

sudo apt install -y ca-certificates curl gnupg

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update

sudo apt install -y docker-ce docker-ce-cli containerd.io

docker --version

sudo systemctl status docker
```
## Step 2: Build Docker Image


docker build -t todo-docker-ui .

## Step 3: Run Container (Production Ready)

docker run -d -p 5000:5000 --name todo-ui-container --restart unless-stopped -v /full/path/to/templates:/app/templates todo-docker-ui

## Step 4: Access the Application

Open your browser: http://localhost:5000

Add tasks, mark done, and view completed tasks


## Step 5: Logs & Verification

Docker version: docker --version

Docker service status: sudo systemctl status docker

Container logs: docker logs todo-ui-container 

## Browser View

![To-Do App UI](images/flask_Todo_app.png)
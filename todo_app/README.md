# Todo App

Web server that outputs "Server started in port NNNN"

## Building the image

docker build -t todo-app:1.2 .

## Deploy to Kubernetes

kubectl apply -f deployment.yaml

## Viewing logs

kubectl logs -f deployment/todo-app
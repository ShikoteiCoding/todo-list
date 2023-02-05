#!/bin/sh

CONTAINER_DB_NAME="api-db"
CONTAINER_API_NAME="api"
VOLUME_NAME="server_note-db"

if [ $( docker ps -a | grep $CONTAINER_DB_NAME | wc -l ) -gt 0 ]; then
    echo "Taking down $CONTAINER_DB_NAME..."
    docker rm $CONTAINER_DB_NAME
else
    echo "Container $CONTAINER_DB_NAME does not exist."
fi

if [ $( docker ps -a | grep $CONTAINER_API_NAME | wc -l ) -gt 0 ]; then
    echo "Taking down $CONTAINER_API_NAME..."
    docker rm $CONTAINER_API_NAME
else
    echo "Container $CONTAINER_API_NAME does not exist."
fi

if [ $( docker volume ls | grep $VOLUME_NAME | wc -l ) -gt 0 ]; then
    echo "Deleting volume $VOLUME_NAME..."
    docker volume rm $VOLUME_NAME
else
    echo "Volume $VOLUME_NAME does not exist."
fi
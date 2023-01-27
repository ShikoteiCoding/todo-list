#!/bin/sh

CONTAINER_NAME="note-db"
VOLUME_NAME="server_note-db"

if [ $( docker ps -a | grep $CONTAINER_NAME | wc -l ) -gt 0 ]; then
    echo "Taking down $CONTAINER_NAME..."
    docker rm $CONTAINER_NAME
else
    echo "Container $CONTAINER_NAME does not exist."
fi

if [ $( docker volume ls | grep $VOLUME_NAME | wc -l ) -gt 0 ]; then
    echo "Deleting volume $VOLUME_NAME..."
    docker volume rm $VOLUME_NAME
else
    echo "Volume $VOLUME_NAME does not exist."
fi
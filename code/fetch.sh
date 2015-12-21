#!/bin/bash

curl -H "Content-Type: application/json" -X POST -d '{"args": ["http://cdn.eso.org/images/screen/eso0202a.jpg", "e0202a"}' http://localhost/api/task/send-task/tasks.fetch_image

curl -H "Content-Type: application/json" --data @fetch_wikipedia.json http://localhost/api/task/send-task/tasks.fetch_image

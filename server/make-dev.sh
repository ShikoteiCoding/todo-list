#!/bin/sh

flask db init
flask db migrate -m "users and notes table"
flask db upgrade
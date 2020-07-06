#!/bin/bash
set -e

if [ "$1" = 'arg' ]; then
   echo "you provided some arguments when you executed docker run"
else
    #else print this
    echo "you did NOT provided any arguments"
fi

python manage.py runserver --noreload
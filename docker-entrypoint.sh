#!/bin/bash


if [ "$1" = 'arg' ]; then
   echo "you provided some arguments when you executed docker run"
else
    #else print this
    echo "you did NOT provided any arguments"


python manage.py runserver --noreload

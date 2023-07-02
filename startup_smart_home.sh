#!/bin/bash

cd home/andrew/Andrew/House/
source env/bin/activate

nohup python telegram_bot.py &

cd Home/

IP_MACHINE='192.168.100.51:8000'

nohup python manage.py runserver $IP_MACHINE &

while true
do
    echo Time is $(date)
    sleep 3600
done

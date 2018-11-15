#!/bin/bash

echo "Esperando a iniciar servidor"

sleep 15

echo "Espera terminada, ahora si iniciando..."

python manage.py migrate
python manage.py runserver $1:$2

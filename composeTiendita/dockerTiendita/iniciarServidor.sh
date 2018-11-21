#!/bin/bash

echo "Esperando a iniciar servidor"

sleep 15

echo "Espera terminada, ahora si iniciando..."

python -u manage.py migrate
python -u manage.py runserver $1:$2

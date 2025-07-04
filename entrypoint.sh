#!/bin/bash

echo "Aguardando o banco de dados..."
while ! nc -z db 5432; do
  sleep 1
done

echo "Banco de dados disponível, rodando migrações..."
python manage.py migrate

echo "Iniciando servidor..."
python manage.py runserver 0.0.0.0:8000

#!/usr/bin/env bash

# Asegúrate de que el entorno virtual está activado (si usas uno)
# source venv/bin/activate  # Descomenta esta línea si usas un entorno virtual

# Instalar las dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Recolectar archivos estáticos para producción
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

# Aplicar migraciones a la base de datos
echo "Aplicando migraciones..."
python manage.py migrate

# Asegurarse de que Gunicorn esté instalado
echo "Instalando Gunicorn (si no está ya instalado)..."
pip install gunicorn

# Ejecutar Gunicorn para servir la aplicación
echo "Iniciando servidor con Gunicorn..."
gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --log-level=info

# Si usas un entorno diferente o necesitas algún otro paso, agrégalo aquí

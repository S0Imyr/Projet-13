FROM python:3.8

EXPOSE 8000

RUN mkdir -p /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG=0
ENV PORT 8000

# Install  requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app.
COPY . /app/

# Collect all static files in app.
RUN python manage.py collectstatic --noinput -c


CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
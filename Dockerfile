FROM python:3.10.4

WORKDIR /code

COPY weather_app .

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
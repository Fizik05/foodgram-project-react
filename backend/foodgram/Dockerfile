FROM python:3.7-slim

WORKDIR /code

COPY . .

RUN pip install -r /code/requirements.txt --no-cache-dir

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]

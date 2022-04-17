FROM python:3.7-slim

WORKDIR /code

COPY ./foodgram .

RUN pip3 install -r /code/requirements.txt --no-cache-dir

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]

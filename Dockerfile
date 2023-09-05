FROM python:3.11.5-alpine3.18

WORKDIR /app

COPY . /app

RUN apk add --no-cache \
    && pip3 install --upgrade pip

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "src/app.py"]
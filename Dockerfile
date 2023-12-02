FROM python:3.11.5-alpine3.18

WORKDIR /app

COPY . /app

RUN apk add --no-cache \
    musl-dev \
    && pip3 install --upgrade pip

RUN apk add --no-cache postgresql-dev

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["/app/init-db.sh"]
FROM python:3.10.12-alpine

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    libsodium-dev \
    libsecp256k1-dev \
    gmp-dev

COPY ./backend/requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY ./docker/backend/entrypoint.sh entrypoint.sh
RUN chmod +x /entrypoint.sh
# RUN chmod +x  manage.py

EXPOSE 8000

CMD ["/entrypoint.sh"]

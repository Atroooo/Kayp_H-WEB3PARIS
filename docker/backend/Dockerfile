FROM python:alpine

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    python3-dev

COPY ./backend/requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY ./docker/backend/entrypoint.sh entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

CMD ["/entrypoint.sh"]

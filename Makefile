.PHONY: all build rebuild stop stop volumes fclean down

all: build up

build:
		docker-compose -f docker-compose.yml build

up:
		docker-compose -f docker-compose.yml up -d

stop:
		docker-compose -f docker-compose.yml stop

fclean:
		docker-compose -f docker-compose.yml down -v --rmi all --remove-orphans

down:
		docker-compose -f docker-compose.yml down

rebuild:
		docker-compose -f docker-compose.yml build --no-cache

re: fclean rebuild all
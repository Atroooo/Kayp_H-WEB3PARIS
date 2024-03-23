FROM node:16

WORKDIR /usr/src/app

RUN npm install -g webpack webpack-cli webpack-dev-server
RUN apt-get update

COPY ./frontend/package.json .

RUN npm install

COPY ./frontend .

EXPOSE 3000

CMD ["npm", "run", "dev"]
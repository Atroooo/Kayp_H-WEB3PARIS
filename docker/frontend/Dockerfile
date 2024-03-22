FROM node:14

WORKDIR /usr/src/app

RUN npm install -g webpack webpack-cli webpack-dev-server

RUN npm install
RUN npm install express 

RUN npm install -s flag-icons

COPY ./frontend .

EXPOSE 3000

CMD ["npm", "run", "dev"]
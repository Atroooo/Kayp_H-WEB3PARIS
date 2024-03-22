FROM node:14

WORKDIR /usr/src/app

RUN npm install -g webpack webpack-cli webpack-dev-server

COPY ./frontend .

EXPOSE 3000

CMD ["npm", "run", "dev"]
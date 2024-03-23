FROM node:14

WORKDIR /usr/src/app

RUN npm install -g webpack webpack-cli webpack-dev-server
RUN apt-get update

COPY ./frontend/package*.json .

RUN npm install
# RUN npm install vite
# RUN npm install react
# RUN npm install -s flag-icons

RUN npm run build

COPY ./frontend .

EXPOSE 3000

CMD ["npm", "run", "dev"]
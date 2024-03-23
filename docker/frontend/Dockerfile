FROM node:21

EXPOSE 5173

WORKDIR /usr/src/app

COPY ./frontend/package*.json .
COPY ./frontend/ .

#RUN npm install -g npm@9.5.0 -s
RUN npm install -s

CMD [ "npm", "run", "dev" ]
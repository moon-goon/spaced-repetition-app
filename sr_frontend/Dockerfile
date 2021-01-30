FROM node:13.12.0-alpine
WORKDIR /app/sr_frontend

COPY package.json ./
RUN npm install -g gulp
RUN npm install react-scripts@3.4.1 -g
RUN npm install
COPY . ./
EXPOSE 3000

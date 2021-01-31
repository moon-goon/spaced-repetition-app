FROM node:14.4.0-alpine3.10

WORKDIR /app/sr_frontend
COPY package.json .
COPY package-lock.json .
COPY . .
RUN npm i
RUN npm run build
EXPOSE 3000
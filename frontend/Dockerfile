FROM node:20

WORKDIR /app/frontend

COPY package.json yarn.lock ./

RUN yarn --ignore-platform

EXPOSE 8080

COPY . .

CMD ["yarn", "dev"]

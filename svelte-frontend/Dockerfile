FROM node:18 AS build

WORKDIR /app

COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
RUN npm run build

EXPOSE 3000
CMD ["node", "build/index.js"]

# FROM nginx:1.23-alpine
# COPY --from=build /app/public /usr/share/nginx/html

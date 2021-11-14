FROM node:14

RUN npm install -g serve
WORKDIR /app

RUN npm install -g npm@8

# copy requirements and install dependancies
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

EXPOSE 8080
CMD ["serve", "-s", "dist", "-l", "8080"]

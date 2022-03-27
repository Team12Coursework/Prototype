FROM node:16

# install serve globally, serve will be used to serve the application pages
RUN npm install -g serve
WORKDIR /app

# update npm version to the version used on local machine
RUN npm install -g npm@8

# copy requirements and install dependancies
COPY package*.json ./
RUN npm install

COPY . .
# build and pack the project for production, this includes pruning Tailwind classes
# and minifying all of the Javascript code
RUN npm run build

CMD serve -s dist -p 5000

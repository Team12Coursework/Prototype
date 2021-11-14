FROM node:14

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

# expose the serve to port 8080
EXPOSE 8080
CMD ["serve", "-s", "dist", "-l", "8080"]

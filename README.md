# CharacterConnect Prototype

This Github repository contains all the code relating to the CharacterCount prototype. This prototype is due on 2021-11-14.

# Running the project

This section covers how to run each section of the CharacterCount project.

## Docker

(WIP, this section is not currently finished yet, we will complete this later in the project.)

For viewing the production build locally, there is a provided docker-compose.yml file. In order to use this file, you must have Docker, and Docker-compose installed. Once those have been installed, you can simply run

`sudo docker-compose up --build`

which will build and run the entire application.

## Frontend

The frontend was created using the Vue-CLI setup tool, so all of the relevant folder structure for properly building the project has been automatically generated.

### Testing

To run a testing version of the frontend code, you should have npm installed. To install the dependancies for the frontend, navigate to the frontend folder and run `npm install --save`. This will install all the relevant dependencies, as outlined in `package.json` and `package-lock.json`. After the dependancies have been installed, running `npm run serve` will build and run a testing version of the frontend.

### Production

Before running the production code, you will need all of the testing dependancies installed as-well as serve. Please follow the installation procedure in the [Testing](#Testing) section first. Once the testing dependancies have been installed, serve can be installed with `npm install -g serve`. 

When testing the code for a production environment, the code will have to be built and pruned first. This process involves [tree shaking](https://webpack.js.org/guides/tree-shaking/) and compression to reduce the final build size. This means that building for a production environment will take more time than the debug server. To build the project, please run `npm run build`. 

After building the project, a dist directory will have been created. In order to serve this like the testing server, you can run `serve -s dist`.

More information about this can be found [here](https://cli.vuejs.org/guide/deployment.html#general-guidelines)

## Backend
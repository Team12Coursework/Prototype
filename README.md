<h1 align="center">
    Character Connect
</h1>

<h2 align="center">
    Team 12 CS2TP Coursework
</h2>

# Running the project

This project provides a `docker-compose.yml` script. For locally testing the project, you are able to run this script using `sudo docker-compose up --build`.

Running the project requires a `.env` file to be placed in the root directory. Assuming the project is running locally. The following `.env` file may be used for a default configuration.

```
DEBUG=1
POSTGRES_USER=postgres
POSTGRES_PASSWORD=aaaf53ea-aab5-11ec-b909-0242ac120002
DATABASE_URI=postgresql://postgres:aaaf53ea-aab5-11ec-b909-0242ac120002@database:5432/postgres
```
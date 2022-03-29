from multiprocessing import connection
from time import sleep
import json

import docker
import psycopg2
from passlib.context import CryptContext


"""
Small script to start some Docker containers for testing. Running this script will start
PostgreSQL and a Redis instance.
"""

# default connection authentication for the local database
connection_auth: dict[str, str] = {
    'user':     'postgres',
    'host':     'localhost',
    'password': 'aaaf53ea-aab5-11ec-b909-0242ac120002',
    'database': 'postgres',
}


def create_default_users(default_password: str = 'password') -> None:
    """function to create default users in the database"""

    context = CryptContext(schemes=['sha256_crypt'])
    password_hash = context.hash(default_password)
    users = [
        ['user_one', password_hash, 'user.one@gmail.com'],
        ['user_two', password_hash, 'user.two@gmail.com'],
    ]

    with psycopg2.connect(**connection_auth) as connection:
        with connection.cursor() as cursor:
            cursor.executemany('INSERT INTO users_tab(username, password, email) VALUES (%s, %s, %s)', users)
    connection.close()

def create_schema() -> None:
    """function to create the database schema from the SQL file located in data/schema.sql"""
    with open('data/schema.sql') as file:
        schema: str = file.read()

    with psycopg2.connect(**connection_auth) as connection:
        with connection.cursor() as cursor:
            cursor.execute(schema)
    connection.close()


def add_postgres_dictionary() -> None:
    """function to insert the dictionary into the PostgreSQL database"""
    with open('data/dictionary.txt') as file:
        data: list[str] = file.readlines()

    # formatting args into a COPY statement instead of an INSERT will dramatically
    # decrease insert time.
    args = ','.join(f"($${line}$$, NULL)" for line in data)
    with psycopg2.connect(**connection_auth) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f'INSERT INTO words_tab VALUES {args}')
    connection.close()


def postgres():
    """Function starts a PostgreSQL docker container.
    The started container will have the following login details:
    username: postgres
    password: cc123
    database: character_count"""

    client = docker.from_env()
    container = client.containers.run(
        'postgres:latest',
        auto_remove=True,
        detach=True,
        ports={'5432/tcp': 5432},
        remove=True,
        name='test_database',
        environment = [
            f'POSTGRES_USER={connection_auth["user"]}',
            f'POSTGRES_PASSWORD={connection_auth["password"]}',
            f'POSTGRES_DB={connection_auth["database"]}'
        ]
    )

    print('created PostgreSQL container, waiting for startup...')

    return container


if __name__ == '__main__':
        print('starting postgres container...')
        postgres_container = postgres()
        sleep(10)

        print('finished starting postgres container, now available to connect')
        print('bulk inserting data into database...')

        create_schema()
        add_postgres_dictionary()
        create_default_users()

        print('finished inserting data into database')

        # use a try/ finally here because i've accidentally
        # ctrl-C'd this to stop the containers too many times.
        try:
            inp = input('press any button to stop database...')
        finally:
            postgres_container.stop()

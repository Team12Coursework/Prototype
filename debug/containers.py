from time import sleep

import docker

"""
Small script to start some Docker containers for testing. Running this script will start
PostgreSQL and a Redis instance.
"""

def postgres() -> docker.models.containers.Container:
    """
    Function starts a PostgreSQL docker container.
    The started container will have the following login details:
    username: postgres
    password: cc123
    database: character_count
    """

    client: docker.DockerClient = docker.from_env()
    container: docker.models.containers.Container = client.containers.run(
        'postgres:latest',
        auto_remove=True,
        detach=True,
        ports={'5432/tcp': 5432},
        remove=True,
        name='test_database',
        environment = [
            'POSTGRES_USER=postgres',
            'POSTGRES_PASSWORD=cc123',
            'POSTGRES_DB=character_connect'
        ]
    )

    print('created PostgreSQL container, waiting for startup...')

    return container


def redis() -> docker.models.containers.Container:
    """function starts a Redis message queue docker container"""

    client: docker.DockerClient = docker.from_env()
    container: docker.models.containers.Container = client.containers.run(
        'redis:latest',
        auto_remove=True,
        detach=True,
        ports={'6379/tcp': 6379},
        remove=True,
        name='test_redis',
    )

    return container


if __name__ == '__main__':
        print('starting redis container...')
        redis_container = redis()

        print('starting postgres container...')
        postgres_container = postgres()

        # use a try/ finally here because i've accidentally
        # ctrl-C'd this to stop the containers too many times.
        try:
            inp = input('press any button to stop database...')
        finally:
            postgres_container.stop()
            redis_container.stop()
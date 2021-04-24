from typing import Container
from azure.cosmos import CosmosClient, PartitionKey
from config import ENDPOINT, KEY


def database():
    client = CosmosClient(ENDPOINT, KEY)

    default_database_name = 'FastApiDB'
    database = client.create_database_if_not_exists(id=default_database_name)

    return database


def container():
    db = database()

    default_container_name = 'FastApiContainer'
    container = db.create_container_if_not_exists(
        id=default_container_name,
        partition_key=PartitionKey(path='/id'),
        offer_throughput=400
    )

    return container
    
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
        partition_key=PartitionKey(path='/uid'),
        offer_throughput=400
    )

    return container


def create(items_to_create):
    cont = container()

    for item in items_to_create:
        cont.create_item(body=item)

    return

def read(items_to_read):
    cont = container()

    for item_to_read in items_to_read:
        item_response = cont.read_item(item=item_to_read['id'], partition_key=item_to_read['uid'])
        request_charge = cont.client_connection.last_response_headers['x-ms-request-charge']
        print('Read item with id {0}. Operation consumed {1} request units'.format(item_response['id'], (request_charge)))

    return

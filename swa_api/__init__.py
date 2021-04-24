from helper import container

CONTAINER = container()

def create(items_to_create):
    if (type(items_to_create) == list):
        for item in items_to_create:
            _create(item)
    else:
        _create(items_to_create)
    return

def _create(item_to_create):
    CONTAINER.create_item(body=item_to_create)
    return

def read(items_to_read):
    if (type(items_to_read) == list):
        for item_to_read in items_to_read:
            _read(item_to_read)
    else:
        _read(items_to_read)
    return

def _read(item_to_read):
    CONTAINER.read_item(item=item_to_read['id'], partition_key=item_to_read['id'])
    CONTAINER.client_connection.last_response_headers['x-ms-request-charge']
    return

def delete(items_to_delete):
    if (type(items_to_delete) == list):
        for item in items_to_delete:
            _delete(item)
    else:
        _delete(items_to_delete)
    return

def _delete(item_to_delete):
    CONTAINER.delete_item(item=item_to_delete['id'], partition_key=item_to_delete['id'])
    return

def replace(items_to_replace):
    if (type(items_to_replace) == list):
        for item in items_to_replace:
            _replace(item)
    else:
        _replace(items_to_replace)
    return

def _replace(item_to_replace):
    CONTAINER.replace_item(body=item_to_replace, item=item_to_replace['id'], partition_key=item_to_replace['id'])
    return
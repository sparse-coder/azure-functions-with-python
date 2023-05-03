import uuid
from azure.storage.blob import BlobServiceClient, generate_blob_sas
from io import BytesIO

class BlobConnnection:
    def __init__(self, conn_str) -> None:
        self.__bsc = BlobServiceClient.from_connection_string(conn_str)
    

    def write_blob(self, container, data):
        ...

    def get_blob_sas(self, blob_name):
        ...

    def close_connection(self):
        self.__bsc.close()


def write_blob(conn_str, container, data):
    # Create the BlobServiceClient object
    b_name = str(uuid.uuid4()) + ".json"
    bsc = BlobServiceClient.from_connection_string(conn_str)
    bc = bsc.get_blob_client(container=container, blob=b_name)
    bc.upload_blob(BytesIO(data.encode()))
    print()

def get_sas_uri_to_blob(conn_str, container, b_name):
    ...

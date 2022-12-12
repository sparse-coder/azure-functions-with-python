import os, uuid
from azure.storage.blob import BlobServiceClient
from io import BytesIO

def write_blob(conn_str, container, data):
    # Create the BlobServiceClient object
    b_name = str(uuid.uuid4()) + ".json"
    bsc = BlobServiceClient.from_connection_string(conn_str)
    bc = bsc.get_blob_client(container=container, blob=b_name)
    bc.upload_blob(BytesIO(data.encode()))
    print()
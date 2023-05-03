import logging
import os
import azure.functions as func
from .scrapper import scrape
from .blob_conn_manager import write_blob

blob_conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container = os.getenv("CONTAINER")
write_to_blob = os.getenv("WRITE_TO_BLOB")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('We have recieved a request')
    try:
        url = req.params.get('url')
        if url:
            res = scrape(url)
            if write_to_blob:
                write_blob(blob_conn_str, container, res)
            return func.HttpResponse(res)

        return func.HttpResponse(
                "Well! to work properly we need a URL in query",
                status_code=200
        )
    except :
        return func.HttpResponse(
            "Oh! It's 500 😥. The programmer didn't anticipate this!",
            status_code=500
        )

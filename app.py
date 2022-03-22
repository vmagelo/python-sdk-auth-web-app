import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
app = Flask(__name__)


# If the app is being run locally, load settings from .env file
if ( os.getenv('FLASK_ENV') == 'development'):
    print("Loading environment variables from .env file")
    load_dotenv(".env")


azure_credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(
   account_url="https://vmagelowebapp.blob.core.windows.net",
   credential=azure_credential)
container_client = blob_service_client.get_container_client("photos")




@app.route('/')
def index():
   print('Request for index page received')

   blob_list = container_client.list_blobs()
   #for blob in blob_list:
   #    print("\t" + blob.name + "\t" + blob.size + blob.last_modified + blob.content_settings.content_type)

   return render_template('index.html', blobs = blob_list)


if __name__ == '__main__':
    app.run()
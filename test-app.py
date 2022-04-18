import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

app = Flask(__name__)

@app.route('/')
def hello_world():
   if (os.getenv('FLASK_ENV') == 'development'):
      print("Flask development environment detected.")
      load_dotenv()
      test_var = os.getenv("TESTVAR")
      return "Hello dev! Your variable = " + str(test_var)
   else:
      print("Flask production environment detected.")
      test_var = os.getenv("TESTVAR")
      return "Hello prod! Your variable = " + str(test_var)

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')
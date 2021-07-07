import contextlib

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore import Client


@contextlib.contextmanager
def get_firestore_client():
    from wsgi import settings
    cred = credentials.Certificate(settings.gcp_certificate_path)
    firebase_admin.initialize_app(cred)
    firestore_client: Client = firestore.client()
    yield firestore_client
    firestore_client.close()

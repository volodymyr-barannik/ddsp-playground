import tensorflow as tf
import gs as gs

filename = "gs://tfds-data/datasets/nsynth/gansynth_subset.f0_and_loudness:2.3.0"

from google.cloud import storage

import os
from urllib.parse import urlparse

def decode_gcs_url(url):
    p = urlparse(url)
    path = p.path[1:].split('/', 1)
    bucket, file_path = path[0], path[1]
    return bucket, file_path

def download_blob(url):
    if url:
        storage_client = storage.Client()
        bucket, file_path = decode_gcs_url(url)
        bucket = storage_client.bucket('tfds-data')
        blob = bucket.blob(file_path)
        blob.download_to_filename('nsynth_dataset')

download_blob(filename)

with tf.io.gfile.GFile(filename, "r") as f:
        content = f.read()
        with open("nsynth_dataset", 'w') as savef:
                savef.write(content)
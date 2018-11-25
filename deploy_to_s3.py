# From: https://jasonstitt.com/codebuild-pelican-blog-updates
import mimetypes
import os

import boto3

from multiprocessing.pool import ThreadPool


bucket = 'stage.chriserickson.me'
s3 = boto3.resource('s3')

os.chdir('output')
filepaths = (os.path.join(root, filename)[2:] for root, dirs, files in os.walk('.') for filename in files)

def put_file(filepath):
    key = filepath
    content_type = mimetypes.guess_type(filepath)[0] or 'text/plain'
    if filepath.endswith('.html') and filepath != 'index.html':
        key = filepath[:-len('.html')]
    s3.Object(bucket, key).put(
        Body=open(filepath, 'rb'),
        ContentType=content_type,
        CacheControl='max-age=3600',
    )

ThreadPool(10).map(put_file, filepaths)

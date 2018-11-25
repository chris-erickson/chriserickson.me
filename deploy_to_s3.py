# From: https://jasonstitt.com/codebuild-pelican-blog-updates
import mimetypes
import os

import boto3

from multiprocessing.pool import ThreadPool

# TODO: Support stage/prod input to select the right bucket
# Short lifetime on html, longer on anything else
# TODO: Some print statements here to know what's going on here: https://circleci.com/gh/chris-erickson/chriserickson.me/24
# TODO: Utility to check for skip dirs (.webassets-cache, less, js.NOT.min) - or maybe jsut delete it on build, in makefile
# TODO: Utility to check for skip paths ()

bucket_name = 'stage.chriserickson.me'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket)

os.chdir('output')
filepaths = (os.path.join(root, filename)[2:] for root, dirs, files in os.walk('.') for filename in files)

def put_file(filepath):
    key = filepath
    content_type = mimetypes.guess_type(filepath)[0] or 'text/plain'
    if filepath.endswith('.html') and filepath != 'index.html':
        key = filepath[:-len('.html')]
    s3.Object(bucket_name, key).put(
        Body=open(filepath, 'rb'),
        ContentType=content_type,
        CacheControl='max-age=3600',
    )

# Clear out the bucket
bucket.objects.all().delete()

print("Bucket: {}".format(bucket_name))
print("Filepaths: {}".format(filepaths))

# Upload the files
ThreadPool(10).map(put_file, filepaths)

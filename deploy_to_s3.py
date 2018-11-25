# From: https://jasonstitt.com/codebuild-pelican-blog-updates
import mimetypes
import os
import sys

import boto3

from multiprocessing.pool import ThreadPool

stage = sys.argv[1] or "stage"

# TODO: Support stage/prod input to select the right bucket
# Short lifetime on html, longer on anything else

if stage == "stage":
    bucket_name = 'stage.chriserickson.me'
else:
    bucket_name = "www.chriserickson.me"


print("Uploading files to {} using bucket {}".format(stage, bucket_name))

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

os.chdir('output')
filepaths = (os.path.join(root, filename)[2:] for root, dirs, files in os.walk('.') for filename in files)

EXCLUDE_FILEPATHS = (
    "theme/.webassets-cache",
    "theme/js/site.js",
    "theme/less",
    "theme/vendor",
)

def should_remove_extension(filepath):
    return filepath and filepath.endswith('.html')


def should_copy_file_with_path(filepath):
    return not any(ex in filepath for ex in EXCLUDE_FILEPATHS)


def put_file(filepath):
    key = filepath
    content_type = mimetypes.guess_type(filepath)[0] or 'text/plain'

    print("Filepath: {}".format(filepath))
    print("Content-Type: {}".format(content_type))

    if should_remove_extension(filepath):
        key = filepath[:-len('.html')]

    if should_copy_file_with_path(filepath):
        s3.Object(bucket_name, key).put(
            Body=open(filepath, 'rb'),
            ContentType=content_type,
            CacheControl='max-age=3600',
        )

# Clear out the bucket
bucket.objects.all().delete()

# Upload the files
ThreadPool(10).map(put_file, filepaths)

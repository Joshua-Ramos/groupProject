from uuid import uuid4
import boto
import os.path
from flask import current_app as app
from werkzeug.utils import secure_filename



def s3_upload(source_file, upload_dir=None, acl='public-read'):
    """ Uploads WTForm File Object to Amazon S3
        Expects following app.config attributes to be set:
            S3_KEY              :   S3 API Key
            S3_SECRET           :   S3 Secret Key
            S3_BUCKET           :   What bucket to upload to
            S3_UPLOAD_DIRECTORY :   Which S3 Directory.
        The default sets the access rights on the uploaded file to
        public-read.  It also generates a unique filename via
        the uuid4 function combined with the file extension from
        the source file.
    """

    if upload_dir is None:
        upload_dir = app.config["S3_UPLOAD_DIRECTORY"]

    filename = source_file.data.filename.replace('_','')
    filename = source_file.data.filename.replace(' ', '')
    source_filename = secure_filename(filename)

    destination_filename = source_filename

    # Connect to S3 and upload file.
    conn = boto.connect_s3(app.config["S3_KEY"], app.config["S3_SECRET"])
    b = conn.get_bucket(app.config["S3_BUCKET"])

    sml = b.new_key("/".join([upload_dir, destination_filename]))
    sml.set_contents_from_string(source_file.data.read())
    sml.set_acl(acl)

    return destination_filename

#Downloads the file given by "filename" to the current directory from AWS S3
def s3_download(filename):
    upload_dir = app.config["S3_UPLOAD_DIRECTORY"]
    conn = boto.connect_s3(app.config["S3_KEY"], app.config["S3_SECRET"])
    bucket = conn.get_bucket(app.config["S3_BUCKET"])
    keyname = "/".join([upload_dir, filename])
    key = bucket.get_key(keyname)
    key.get_contents_to_filename(filename)

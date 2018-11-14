from . import Aws
import os
from botocore.exceptions import ClientError


class SimpleStorage(Aws):
    def __init__(self, bucket_name, profile_name=None, **kwargs):
        super().__init__("lambda", profile_name, **kwargs)
        self.bucket_name = bucket_name

    def get_objects(self, object_path):
        return self.client.list_objects(Bucket=self.bucket_name, Prefix=object_path, Delimiter="/")

    def read_object(self, object_path, ext):
        return self.client.get_object(Bucket=self.bucket_name, Key=object_path)["Body"].read()

    def create_object(self, object_path, data):
        self.client.put_object(Bucket=self.bucket_name, Key=object_path, Body=data)

    def delete_object(self, object_path):
        self.client.delete_object(Bucket=self.bucket_name, Key=object_path)

    def generate_presigned_url(self, object_path, expiration=30):
        return self.client.generate_presigned_url(ClientMethod='get_object', ExpiresIn=expiration,
                                                  Params={"Bucket": self.bucket_name, "Key": object_path})

    def check_existence(self, object_path):
        try:
            self.client.get_object(Bucket=self.bucket_name, Key=object_path)
            return True
        except ClientError:
            return False

    def download_file(self, object_path, download_path):
        self.client.download_file(Filename=download_path, Bucket=self.bucket_name, Key=object_path)

    def upload_file(self, object_path, file_path, remove=False):
        self.client.upload_file(Filename=file_path, Bucket=self.bucket_name, Key=object_path)
        if remove:
            os.remove(file_path)

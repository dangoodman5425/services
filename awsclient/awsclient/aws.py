import os
from boto3 import client, session


class Aws:
    def __init__(self, service_name, profile_name=None, **kwargs):
        if not profile_name:
            aws_key = kwargs.get("AWS_ACCESS_KEY_ID", os.environ.get("AWS_ACCESS_KEY"))
            aws_secret = kwargs.get("AWS_SECRET_AWS_KEY", os.environ.get("AWS_ACCESS_SECRET"))
            self.client = client(service_name=service_name, aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)
        else:
            self.session = session.Session(profile_name=profile_name)
            self.client = self.session.client(service_name=service_name)

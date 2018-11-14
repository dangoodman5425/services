from .aws import Aws
import simplejson as json


class AwsLambda(Aws):
    def __init__(self, profile_name=None, **kwargs):
        super().__init__("lambda", profile_name, **kwargs)

    def run(self, function_name, payload):
        return json.load(self.client.invoke(FunctionName=function_name, Payload=payload)["Payload"])

    def run_async(self, function_name, payload):
        return json.load(self.client.invoke(FunctionName=function_name, InvocationType="Event",
                                            Payload=payload))["Payload"]

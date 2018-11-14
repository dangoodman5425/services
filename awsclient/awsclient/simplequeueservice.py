from . import Aws

class SimpleQueue(Aws):
    def __init__(self, queue_name, profile_name=None, **kwargs):
        super().__init__("sqs", profile_name, **kwargs)
        self.queue = self.client.get_queue(queue_name)
   
    def send_message(self, message_body, delay_time=0):
        message = self.queue.new_message(message_body)
        response = self.queue.write(message, delay_time)
        return response.id

    def get_messages(self):
        return self.queue.get_messages()

    def delete_message(self, message):
        self.queue.delete_message(message)

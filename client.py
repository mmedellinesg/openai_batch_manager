from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def upload_file(self, filepath):
        return self.client.files.create(file=open(filepath, 'rb'), purpose='batch')

    def create_batch(self, file_id, purpose, endpoint='/v1/chat/completions', completion_window='24h'):
        return self.client.batches.create(
            input_file_id=file_id,
            endpoint=endpoint,
            completion_window=completion_window,
            metadata={'description': purpose}
        )

    def get_batch_status(self, batch_id):
        return self.client.batches.retrieve(batch_id)

    def download_results(self, batch_id, out_path):
        batch = self.get_batch_status(batch_id)
        if batch.status == 'completed':
            batch_obj = self.client.batches.retrieve(batch_id)
            file = self.client.files.content(batch_obj.output_file_id)
            with open(out_path, 'wb') as f:
                f.write(file.text)
            return batch.output_file_id
        return False

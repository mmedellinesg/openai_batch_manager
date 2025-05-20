# batch_manager.py
from .logger import LogFileManager
from .client import OpenAIClient

class BatchManager:
    def __init__(self, api_key, log_path="logs/gpt_batch_requests.csv"):
        self.client = OpenAIClient(api_key)
        self.logger = LogFileManager(log_path)

    def submit_batch(self, infile, purpose=''):
        uploaded = self.client.upload_file(infile)
        batch = self.client.create_batch(uploaded.id, purpose)
        self.logger.log_submission(batch.id, infile, uploaded.id, purpose)
        print(f"Uploaded file: {uploaded.id}")
        print(f"Submitted batch: {batch.id}")
        return uploaded.id, batch.id

    def check_status(self, batch_id):
        return self.client.get_batch_status(batch_id)

    def download_if_ready(self, batch_id, out_path):
        self.client.download_results(batch_id, out_path)
        # Update the log file with the status
        self.logger.update_status(batch_id, 'completed')
        print(f"Downloaded results for batch: {batch_id}")
        return True

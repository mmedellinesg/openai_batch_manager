# batch_manager.py
from .logger import LogFileManager
from .client import OpenAIClient
import os
import warnings
from datetime import datetime

class BatchManager:
    def __init__(self, api_key, log_path="logs/gpt_batch_requests.csv"):
        self.client = OpenAIClient(api_key)
        self.logger = LogFileManager(log_path)

    def submit_batch(self, infile, purpose='', duplicate_skip=True):
        log_df = self.logger.df

        # Check if the file has already been submitted
        already_logged = log_df['infile'].apply(os.path.basename).tolist()
        this_file = os.path.basename(infile)
        if this_file in already_logged:
            # Get batch ID of the already logged file
            batch_id = log_df.loc[log_df['infile'] == infile, 'id'].values[0]
            batch_status = log_df.loc[log_df['id'] == batch_id, 'status'].values[0]
            if batch_status != 'failed':
                warnings.warn(f"File {this_file} has already been submitted with batch ID {batch_id} and status {batch_status}.")
                
                if duplicate_skip:
                    raise ValueError(f"File '{this_file}' has already been submitted — aborting.")

        uploaded = self.client.upload_file(infile)
        batch = self.client.create_batch(uploaded.id, purpose)
        self.logger.log_submission(batch.id, infile, uploaded.id, purpose)
        print(f"Uploaded file: {uploaded.id}")
        print(f"Submitted batch: {batch.id}")
        return uploaded.id, batch.id

    def check_status(self, batch_id, update_log=True):
        report = self.client.get_batch_status(batch_id)
        print(f"Batch ID: {batch_id}")
        print(f"Submitted: {datetime.fromtimestamp(report.created_at).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Status: {report.status}")
        if update_log:
            self.logger.update_status(batch_id, report.status)
        return self.client.get_batch_status(batch_id)

    def download_if_ready(self, batch_id, out_path):
        self.client.download_results(batch_id, out_path)
        # Update the log file with the status
        self.logger.update_status(batch_id, 'completed')
        print(f"Downloaded results for batch: {batch_id}")
        return True

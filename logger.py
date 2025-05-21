import pandas as pd
import os
from datetime import datetime

class LogFileManager:
    def __init__(self, path):
        self.path = path
        self.columns = [
            'id', 'submission_datetime', 'purpose','infile','infile_id','status','status_datetime','outfile','outfile_id'
        ]
        self._ensure_exists()

    def _ensure_exists(self):
        if not os.path.exists(self.path):
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.path, index=False)
        else:
            df = pd.read_csv(self.path)
        self.df = df

    def log_submission(self, batch_id, infile, infile_id, purpose, status='created'):
        df = pd.read_csv(self.path)
        row = pd.DataFrame([[
            batch_id, datetime.now().isoformat(), purpose, infile, infile_id, status, datetime.now().isoformat(), '', ''
        ]], columns=self.columns)
        df = pd.concat([df, row], ignore_index=True)
        df.to_csv(self.path, index=False)
        self.df = df
        print(f"Logged submission: {batch_id}")

    def update_status(self, batch_id, status):
        df = pd.read_csv(self.path)
        if batch_id in df['id'].values:
            df.loc[df['id'] == batch_id, 'status'] = status
            df.loc[df['id'] == batch_id, 'status_datetime'] = datetime.now().isoformat()
            df.to_csv(self.path, index=False)
            self.df = df
            print(f"Updated status for batch: {batch_id}")
        else:
            print(f"Batch ID {batch_id} not found in log.")
    
    def update_outfile(self, batch_id, outfile, outfile_id):
        df = pd.read_csv(self.path)
        if batch_id in df['id'].values:
            df.loc[df['id'] == batch_id, 'outfile'] = outfile
            df.loc[df['id'] == batch_id, 'outfile_id'] = outfile_id
            df.to_csv(self.path, index=False)
            self.df = df
            print(f"Updated outfile for batch: {batch_id}")
        else:
            print(f"Batch ID {batch_id} not found in log.")

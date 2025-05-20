import pandas as pd
import os
from datetime import datetime

class LogFileManager:
    def __init__(self, path):
        self.path = path
        self.columns = ['id', 'submission_datetime', 'purpose','infile','status','status_datetime']
        self._ensure_exists()

    def _ensure_exists(self):
        if not os.path.exists(self.path):
            pd.DataFrame(columns=self.columns).to_csv(self.path, index=False)

    def log_submission(self, batch_id, purpose, infile, status='created'):
        log = pd.read_csv(self.path)
        row = pd.DataFrame([[batch_id, datetime.now().isoformat(), purpose, infile, status, datetime.now().isoformat()]], columns=self.columns)
        log = pd.concat([log, row], ignore_index=True)
        log.to_csv(self.path, index=False)

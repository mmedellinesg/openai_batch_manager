import os
import time
from openai import OpenAI


def upload_batch(file_path, api_key, purpose):
    client = OpenAI(api_key)

    # Upload the file
    print(f"Uploading file {file_path} for purpose {purpose}...")
    try:
        batch_input_file = client.files.create(
            file=open(file_path, "rb"),
            purpose=purpose
        )
        batch_input_file_id = batch_input_file.id

        print("File uploaded successfully. Creating batch...")
        try:
            cl = client.batches.create(
                input_file_id = batch_input_file_id,
                endpoint = '/v1/chat/completions',
                completion_window = '24h',
                metadata = {
                    'description': purpose
                }
            )
            print("Batch created successfully.")

            # Check that the batch is created
            time.sleep(1)
            (
                print(f"Batch submitted! ID: {cl.id}") 
                    if cl and hasattr(cl, "id") 
                else print("Batch submission failed.")
            )
            return batch_input_file_id, cl.id

        except Exception as e:
            print(f"Error creating batch: {e}")
            return batch_input_file_id, None
    
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None, None
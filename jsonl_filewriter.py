import json

def write_jsonl_file_from_df(
    df, 
    system,
    col,
    model = "gpt-4.1-mini",
    max_tokens = 4096):
    # Write JSONL file
    jsonl_content = ""
    i = 1
    for idx, entry in df.iterrows():
        jsonl_content += write_jsonl_row(f"request-{i}", model, system, entry[col], max_tokens)
        i += 1
    return jsonl_content


def write_jsonl_row(custom_id, model, system, user_input, max_tokens=4096):
    # Create a single JSONL row
    line = {
        "custom_id": custom_id,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user_input}
            ],
            "max_tokens": max_tokens
        }
    }
    return json.dumps(line) + "\n"
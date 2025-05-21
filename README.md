# OpenAI Batch Manager

This is a simplified OpenAI batch API wrapper with added logging functions and a simplified interface.

# Installation

Install by either cloning or including in your repository as a submodule.

```bash
git clone https://github.com/mmedellinesg/openai_batch_manager
```

```bash
git submodule add https://github.com/mmedellinesg/openai_batch_manager
```

# Usage

This package includes functions to:
1. Write OpenAI batch files from dataframe columns
2. Submit written files and log in a `pandas` dataframe stored as `csv`.
3. Check and update batch task status.
4. Download and log output files when batch tasks are completed.

## Writing batch files
Submitting queries through the OpenAI batch API requires writing them into a `jsonl` file.

If the queries the user want to submit are contained in a dataframe `df`'s column `col`, the whole column can be translated into the correct format with a single function stored in `jsonl_filewriter`:

```python
content = write_jsonl_file_from_df(
    df, 
    system,
    col,
    model = "gpt-4.1-mini",
    max_tokens = 4096)
```

Which returns the jsonl content as a string. We can then export it with:

```python
with open('infile.jsonl','w') as f:
    f.write(content)
```

## BatchManager: A class to simplify interaction with the OpenAI client
The `BatchManager` class can be initiated with the OpenAI API key and the location of the desired `csv` log file:

```python
manager = BatchManager(
    api_key,
    log_path
)
```

With it, the user can submit batch files and log the task's ID in the assigned log file:
```python
manager.submit_batch(infile_path)
```

Check a batch status by ID:
```python
manager.check_status(batch_id)
```

And download the output file when the task is finalized:
```python
manager.download_if_ready(
    batch_id,
    out_path
)
```

The log file can be checked at any time as follows:

```python
manager.logger.df
```

# Example use
See [here](https://github.com/mmedellinesg/openai_batch_manager/blob/e26862849768a7ae55ff21633b9a64174cec512c/examples/Example%20use%20of%20BatchManager.ipynb).

# References
[OpenAI batch API guide](https://platform.openai.com/docs/guides/batch)

# Questions?
Please open an issue if you encounter problems.

# License
This project is licensed under the MIT License.

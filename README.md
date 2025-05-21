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

# Example use
See [here](https://github.com/mmedellinesg/openai_batch_manager/blob/e26862849768a7ae55ff21633b9a64174cec512c/examples/Example%20use%20of%20BatchManager.ipynb).

# License
This project is licensed under the MIT License.

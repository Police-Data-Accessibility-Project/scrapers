# Arguments:

- `get_files` takes 2 necessary arguments: `sav_dir`, and `sleep_time`.

- `sav_dir` : Path to save the data to.

- `sleep_time` : Defined in the `configs.py`, sets how long the script will wait between getting each file.

- `delete` : Useful for debugging issues with `extract_info`, set it to `False` to keep the `url_names.txt` file.

- `debug` : Enables printing of certain tracebacks. Default `False`.

- `name_in_url` : If the name is not in the URL, set `name_in_url=False` when calling.

# Info

`get_files` is the main module.

`REF_get_files` is just a reference script should I need the "intact" version

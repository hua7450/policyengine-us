Fix test_batched.py silently dropping `--batches N` and `--exclude` for folders without subdirectories, which caused duplicated and under-parallelized CI test runs.

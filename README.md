# Server Log Analyze

A beginner Python project that reads a server log file, counts log levels, finds the most common error message, and exports a summary to JSON.

## Features

- Counts INFO, WARNING, and ERROR entries
- Counts occurrences of each error message
- Finds one most common error message
- Writes the analysis results to `summary.json`
- Uses only the Python standard library

## Input format

Each line must contain a date, a time, a log level, and a message:

```text
2026-10-06 10:01:12 INFO Server started
2026-10-06 10:02:03 INFO User login
2026-10-06 10:04:51 ERROR Database connection failed
2026-10-06 10:05:04 WARNING CPU usage high
2026-10-06 10:06:19 ERROR Database connection failed
```

## Usage

Run the program from the project directory:

```bash
cd server-log-analyze
python main.py
```

The program reads `sample.log` and creates or replaces `summary.json` in the current working directory.

## Expected sample results

| Result | Expected value |
|---|---|
| Total entries | 5 |
| INFO | 2 |
| WARNING | 1 |
| ERROR | 2 |
| Most common error | Database connection failed |
| Occurrences of the most common error | 2 |

## Current limitations

- Input must follow the format shown above; blank or malformed lines are not handled yet.
- Relative file paths require running the program from the project directory.
- If error messages tie for the highest count, the first encountered message is selected.
- The no-error output has not yet been polished.

## What I practiced

File reading and writing, lists, string methods, loops, conditions, dictionaries, finding a maximum, and JSON export.

This project was developed as a learning exercise with AI-assisted explanations and debugging.


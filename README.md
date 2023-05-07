# PostgreSQL Database Backup to S3

This Python script connects to a PostgreSQL database, creates backups of all non-template databases, and uploads the backup files to an S3 bucket.

## Requirements

- Python 3.x
- PostgreSQL
- S3 bucket with credentials

## Installation

1. Clone this repository
2. Install the required dependencies with `pip install -r requirements.txt`
3. Copy `env.example` to `.env` and complete environments
4. Run the script with `python app.py`

## Docker

You can also run this script as a Docker container. To build the container, run:

```bash
docker compose up 
```
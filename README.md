# HHVacancies

Search vacancies on HeadHunter and SuperJob and see the average salary in a console table.

## Installation

Python 3.11+ and PIP should be installed.

- Download the source archive from GitHub Releases.
- Unarchive and open your terminal.
- Run the following command:

```bash
pip install -r requirements.txt
```

## Configuration

- Rename `.env.copy` to `.env`.
- Paste your SuperJob secret key into the `SUPERJOB_SECRET_KEY` field.

## Running

- To run the script, execute

```bash
python main.py
```

> The script will run for about 10 minutes, don't think it broke if it's stuck on parsing vacancies for a long time.

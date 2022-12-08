A simple Rock Paper Scissors game which can be played in the browser.

Built with [Python](https://www.python.org/) using [Flask](https://flask.palletsprojects.com/en/2.2.x/installation/) [tutorial code](https://github.com/pallets/flask/tree/main/examples/tutorial) and [SQLite](https://www.sqlite.org/index.html).

## Quick Start

Initialize a python virtual environment and install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Initialize the SQLite database.
```bash
flask --app rps_game init-db
```

Start the development flask web application server.
```bash
flask --app rps_game --debug run
```

Run unit tests
```bash
pytest
```

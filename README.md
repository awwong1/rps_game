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

## Requirements

The basic requirements for the game are:
- Allow two players to enter their names
- One of the players can also be the computer, i.e. player vs computer
- Allow each to play a turn, one at a time, during which the player selects one of the option
from rock, paper, scissors
- During each turn notify who has won and increment the scores
- In addition to implementing basic gameplay, the user must be able to save their game
- Try to be specific to the role you are considering. For example,
    - Front End Engineer: UI focused
    - Back End Engineer: Python or other back end language focused
    - Full Stack Engineer: Incorporate both UI and Back End development
- However, timebox it to 3 hours and let us know how much you were able to achieve and what improvements you would have worked on if you had more time. We would like to read your documentation on this.

## Guidance

- We don’t expect completeness. We are interested in your thought process and problem-solving approach. This coding challenge is a base for the next round of technical discussions.
- We want to assess your coding skills and understand your decisions in the design and implementation of the assignment.
- We value your time and the effort that goes into interviewing. We recommend not to spend more than 3 hours on this, however, it is up to you how you want to work on this coding challenge and come back to us with your solution. What we are interested in is hearing what you were able to achieve in these 3 hours and what further ideas and improvements you would have worked on if you had more time.
- There is no objectively right or wrong approach, and we are not primarily interested in a complete or polished solution. We encourage you to timebox your work to 3 hours or less.
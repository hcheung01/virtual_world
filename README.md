# Virtual World

## Description and features:
* Able to randomly generate a scalable virtual world(Diablo style) with keyboard support!
* User can choose how many levels to create and to go up and down
* User can choose N by N size for each level
* Each block is guarantee to have different items and non repeating
* Each block is guarantee to have different people
* Each block is guarantee to be randomly generated for Solid or Transparent type
* When moving to next block, realtime information will display
* Freedom of movement with keyboard controls

## Important
To run locally, please:
1. `git clone https://github.com/hcheung01/virtual_world.git`
2. `cd into directory`
3. `pip install -r requirements.txt`

## How to play
To start game
`./movement.py` or `python3 movement.py`

1. Pick how many levels
2. Pick how many rows X column per level
3. Press enter to start

## To navigate by keyboard
```
UP - North
DOWN - South
LEFT - East
RIGHT - West

L/R SHIFT - Up one level
L/R CTRL - Down one level
```

## What is missing and why:
* Spent too much time architecting world/engine, so no REST API and database
* Did not add interactive commands to talk to myself
* Did not implement race condition because of no users, only Lorem Ipsum objects in JSON format each block and not have to worry about HTTP request when moving to another block

## What I want to improve
* Create Flask RESTful API with CRUD operations with relational database using SQLalchemy ORM. Then when users type global commands like `yell`, send GET request for all users_id in the room_id and POST request to all users.
* Views to: GET/POST for user, GET/POST/PUT/DELETE coordinates
* Some models for database tables I will want to implement
  - User model with primary key, room_id for last known position
  - History model - primary key, foreign key as user_id, dialog_history, move_history 
  - Room model - primary key, level, row, column, state(Transparent or Block), descriptions, items 
* Mapped current working keyboard function so when users move to new block, POST request to database and update location.

## Files
------
```
.
├── LoremIpsums
│   ├── README.md
│   ├── items.json
│   └── names.json
├── main.py
├── model.py
├── movement.py
├── requirements.txt
├── room.py
└── world.py
```

## Directories
---
Directory Name | Description
---|---
virtualgame/ | Main directory with all python files

## More Info for Python programs
* PEP 8 formatted
* Python Scripts - first line of every file is exactly be exactly 
* `#!/usr/bin/env python3` and executable

## Author
Heindrick Cheung
#!/usr/bin/env python3
"""
Script to run program
"""
from world import World
from pynput.keyboard import Key, Listener


levels = int(input("How many levels? "))
size = int(input("How big for each level? N X N "))
print("Press any of the in-game keys to start..")

w = World(levels, size)
w.generate_rooms()
w.mapped_table()
display_table = w.table_ui()
start_position = {
    "level": 0,
    "row": 0,
    "column": 0
}

def room_type_checker(next_location):
  """
  Check if room is suppose to be blocked
  """

  if next_location:
    x, y, z = next_location
    if w.table[x][y][z].roomType is 'Solid':
      return False
    return True

def output(prev_location, command, size):
  """
  Give instant block location updates from the mapped table of objects
  """

  w.starting_location = start_position
  w.printTable(prev_location, size)
  x, y, z = start_position.values()
  print("Updated GPS coordinates: Level: {} | Row: {} | Column: {} | Traveling: {}\n".format(x+1, y, z, command))
  print(w.table[x][y][z])

keys = {
  Key.right: "EAST",
  Key.left: "WEST",
  Key.down: "SOUTH",
  Key.up: "NORTH",
  Key.shift_r: "UP",
  Key.shift_l: "UP",
  Key.ctrl_r: "DOWN",
  Key.ctrl_l: "DOWN",
  Key.enter: "ENTER"
}

def on_press(key):
  """
  Record on key press event
  """

  pass

def on_release(key):
  """
  record key release event and update player position
  """

  if key == Key.esc:
      # Stop listener
      return False
  if key in keys:
    command = keys[key]
    prev_location = start_position.copy()
    if command is 'NORTH' and start_position['row'] < size - 1:
      start_position['row'] += 1
    elif command is 'SOUTH' and start_position['row'] > 0:
      start_position['row'] -= 1
    elif command is 'WEST' and start_position['column'] > 0:
      start_position['column'] -= 1
    elif command is 'EAST' and start_position['column'] < size - 1:
      start_position['column'] += 1
    elif command is 'UP' and start_position['level'] < levels - 1:
      start_position['level'] += 1
    elif command is 'DOWN' and start_position['level'] > 0:
      start_position['level'] -= 1
    output(prev_location, command, size)

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()



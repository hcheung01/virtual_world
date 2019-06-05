#!/usr/bin/env python3
"""
World Class Module
"""

from room import Room
import random

class World():
  """Blueprint of World instance"""

  def __init__(self, level, size):
    """
    contructor function
    """

    self.blank_table = None
    self.starting_location = None
    self.level = level
    self.size = size
    self.rooms = None

  def generate_rooms(self):
    """
    method to generate list of room instances
    """

    list_of_rooms = [Room() for x in range(self.size)]
    return list_of_rooms

  def mapped_table(self):
    """
    method to map list of room instances to 3d table
    """

    self.table = [[self.generate_rooms() for col in range(self.size)] for row in range(self.level)]

  def table_ui(self):
    """
    method to create a copy of mapped table for display on terminal
    """

    new_table = [[["" for col in row] for row in table] for table in self.table]
    self.blank_table = new_table
    return self.blank_table
  
  def printTable(self, previous_location=None, size=None):
    """
    method to output friendly table and position location indicator
    """

    print('\n\n\n\n\n\n\n\n\n\nYOU START ON SOUTHSIDE FIRST LEVEL...\n')
    position_indicator = '^'
    if previous_location:
      x, y, z = previous_location.values()
      self.blank_table[x][y][z] = ""
    x, y, z = self.starting_location.values()
    self.blank_table[x][y][z] = position_indicator

    n = len(self.blank_table)
    for i in range(n - 1, -1, -1):
      print("\nLevel " + str(i + 1) + '\n')
      m = len(self.blank_table[i])
      for j in range(m - 1, -1, -1):
        print(("[ {:2}] " * size).format(*self.blank_table[i][j]))
        print()


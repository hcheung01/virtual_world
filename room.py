#!/usr/bin/env python3
"""
Room Class Module
"""
import random
import json

class Room:
  """blueprint to create room objects"""

  def __init__(self):
    """
    contructor function
    """
    self.roomType = random.choice(['Transparent', 'Solid'])
    self.roomItems = self.set_generate_items()
    self.people = self.set_generate_people()
    
  def __repr__(self):
    """
    output method
    """

    return '<(roomType: {}, people: {}, roomItem: {})>'.format(
      self.roomType, 
      self.people, 
      self.roomItems)

  def __str__(self):
    """
    friendly output method
    """

    return "Description: {}, Items: {}, People: {}".format(
      self.roomType,
      self.roomItems,
      self.people)

  def set_generate_people(self):
    """
    method to create list of randomly selected people from external JSON
    """

    c = random.choice
    with open('./LoremIpsums/names.json') as f:
      data = json.load(f)
      list_of_names = [name for name in data]
    random_people = [c(list_of_names) for i in range(c(range(1, 10)))]
    return random_people

  def set_generate_items(self):
    """
    method to create list of randomly selected items from external JSON
    """

    with open('./LoremIpsums/items.json') as f:
      data = json.load(f)
      c = random.choice
      random_items = set(c(data) for i in range(c(range(1, 10))))
    return random_items

  def get_items(self):
    """
    getter method to return list of items
    """

    return self.roomItems

  def get_people(self):
    """
    getter method to return list of people
    """
    return self.people

  def getRoomType(self):
    """
    getter method to return room type
    """

    return self.roomType


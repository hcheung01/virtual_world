#!/usr/bin/env python3
import random
import json

class Room:
  def __init__(self):
    self.roomType = random.choice(['Transparent', 'Solid'])
    self.roomItems = self.set_generate_items()
    self.people = self.set_generate_people()
    
  def __repr__(self):
    return '<(roomType: {}, people: {}, roomItem: {})>'.format(
      self.roomType, 
      self.people, 
      self.roomItems)

  def __str__(self):
    return "Description: {}, Items: {}, People: {}".format(
      self.roomType,
      self.roomItems,
      self.people)

  def set_generate_people(self):
    c = random.choice

    with open('./LoremIpsums/names.json') as f:
      data = json.load(f)
      list_of_names = [name for name in data]
    random_people = [c(list_of_names) for i in range(c(range(1, 10)))]
    return random_people

  def set_generate_items(self):
    with open('./LoremIpsums/items.json') as f:
      data = json.load(f)
      c = random.choice
      random_items = set(c(data) for i in range(c(range(1, 10))))
    return random_items

  def get_items(self):
    return self.roomItems

  def get_people(self):
    return self.people

  def getRoomType(self):
    return self.roomType

  def getRoomDescription(self):
    return self.roomItems

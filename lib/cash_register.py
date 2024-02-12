#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount 
    self.total = 0
    self.items = []
  
  def add_item(self, title, price, quantity=1):
    self.total += price*quantity
    for i in range(quantity):
      self.items.append(title)
    self.last_item_price = price
    self.last_item_quantity = quantity
  
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = int((self.total*(100-self.discount))/100)
      print(f"After the discount, the total comes to ${self.total}.")
  
  def void_last_transaction(self):
    for i in range(self.last_item_quantity):
      self.items.pop()
      self.total -= self.last_item_price
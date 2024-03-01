#!/usr/bin/env python3
# lib/shoe.py

class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.color} {self.brand} Shoe (Size {self.size})"

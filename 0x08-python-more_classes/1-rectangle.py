#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width = None, height = None):
        """Initializes a triangle"""
        self._width = width if width is not None else 0
        self._height = height if height is not None else 0


    @property
    def width(self):
        """Gets the rectangle width"""
        return self._width

    @width.setter
    def set_width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if width < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Gets the height"""
        return self._height

    @height.setter
    def set_height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if height < 0:
            raise ValueError("Height must be >= 0")
        self._height = value

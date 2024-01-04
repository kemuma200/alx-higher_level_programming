#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, height, width):
        """Initializes a triangle"""
        self.height = height
        self.width = width


    @property
    def width:
        """Gets the rectangle width"""
        return self.__width

    @width_setter
    def set_width:
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if width < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def set_height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if height < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

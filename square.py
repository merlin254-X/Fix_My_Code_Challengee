#!/usr/bin/python3


class Square():
  """
  Represents a square with width and height properties.
  """

  width = 0
  height = 0

  def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
          setattr(self, key, value)

  def area_of_my_square(self):
    """
    Calculates the area of the square.
    """
    return self.width * self.width

  def perimeter_of_my_square(self):
    """
    Calculates the perimeter of the square.
    """
    return self.width * 4

  def __str__(self):
    """
    Returns a string representation of the square with width and height.
    """
    return "Square(width: %d, height: %d)" % (self.width, self.height)
if __name__ == "__main__":

  s = Square(width=12, height=9)
  print(s)
  print(s.area_of_my_square())
  print(s.perimeter_of_my_square())


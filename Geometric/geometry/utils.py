from .shapes import Circle, Triangle

def get_area(shape):
    return shape.area()

def is_right_triangle(triangle):
    if isinstance(triangle, Triangle):
        return triangle.is_right_angle()
    raise TypeError("The provided shape is not a Triangle")

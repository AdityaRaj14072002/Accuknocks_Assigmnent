class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Usage:
rectangle = Rectangle(5, 10)
for attribute in rectangle:
    print(attribute)

# Output will be:
# {'length': 5}
# {'width': 10}

# This Rectangle class allows iteration over its instances, first returning the length and then the width as specified.
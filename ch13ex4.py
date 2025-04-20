"""To identify image files, write a function called is_image that takes a path and a list of file extensions, and returns
 True if the path ends with one of the extensions in the list. Hint: Use os.path.splitext – or ask a virtual assistant
to write this function for you.
"""

import os

def is_image(path, extensions):
    ext = os.path.splitext(path)[1].lower()
    return ext.strip('.') in extensions

extensions = ['jpg', 'jpeg']

print(is_image('photos/photo1.jpg', extensions))        # True
print(is_image('photos/photo1.jpeg', extensions))       # True
print(is_image('photos/photo1.JPG', extensions))        # True
print(is_image('photos/photo1.png', extensions))        # False
print(is_image('photos/document.txt', extensions))      # False

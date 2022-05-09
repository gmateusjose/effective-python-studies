"""
18. Know how to construct key-dependent default values with __missing__
"""

pictures = {}
path = 'profile_1234.png'

if (handle := pictures.get(path)) is None:
    try:
        handle = open(path, 'a+b')
    except OSError:
        print(f'Failed to open path {path}')
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()


from collections import defaultdict

def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except:
        print(f'Failed to open path {profile_path}')
        raise

pictures = defaultdict(open_picture)
handle = pictures[path]
handle.seek(0)
image_data = handle.read()


class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value

pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()

"""
Things to remember:

- The setdefault method of dict is a bad fit when creating the default value
has high computational cost or may raise exceptions

- The function passed to defaultdict must no require any arguments, which makes
it impossible to have the default value depend on the key being accessed.

- You can define your own dict subclasses with a __missing__ method in order to
construct default values that must know which key was being accessed.
"""

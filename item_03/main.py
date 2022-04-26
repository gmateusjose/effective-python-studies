"""
03. Know the differences between bytes and str
"""

# FIRST EXAMPLE
a = b'h\x65llo'
print(list(a))
print(a)

a = 'a\u0300 propos'
print(list(a))
print(a)

# SECOND EXAMPLE
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode('utf-8')
    return bytes_or_str

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode('utf-8')
    return bytes_or_str

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))

"""
Things to remember:

- bytes contains sequences of 8-bit values, and str contains sequences of Unicode
code points.

- Use helper functions to ensuer that the inputs you operate on are the type of
character sequence that you expect (8-bit values, utf-8-encoded strings,
Unicode code points, etc).

- bytes and str instances can't be used together with operators (like, >, ==, +,
and %)

- If you want to read or write binary data to/from a file, always open the file
using a binary mode (like 'rb' or 'wb').

- If you want to read or write Unicode data to/from a file, be careful about
your system's default text encoding. Explicitly pass the encoding parameter to
open if you want to avoid surprises
"""

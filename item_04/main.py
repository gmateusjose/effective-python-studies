"""
04. Prefer interpolated F-strings over C-style format strings and str.format
"""
# First Example
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))


"""
Things to remember:

- C-style format strings that use the % operator suffer from a variety of gotchas
and verbosity problems.

- The str.format method introduces some useful concepts in its formatting
specifiers mini language, but it otherwise repeats the mistakes of C-style
format strings and should be avoided.

- F-strings are a new syntax for formatting values into strings that solves the
biggest problems with C-style format strings.

- F-strings are succint yet powerful because they allow for arbitrary python 
expressions to be directly embedded within format specifiers.
"""

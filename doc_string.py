# docstrings is a triple quoted string placed as the very first statement of the function,class or module
def greet (name):
  """ Return a greeting string for the given name."""
  return f'Hello, {name}!'

print(greet('Alice'))
print(greet.__doc__)
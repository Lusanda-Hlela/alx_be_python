# Drawing Patterns with Nested Loops

# this is the parameter that will be used for generating rows
square_rows = int(input("Enter the size of the pattern: "))

square_columns = square_rows

while square_rows:
  for i in range(square_columns):
    print("*", end="")
  square_rows -= 1
  if square_rows != 0:
    print()
  else:
    break
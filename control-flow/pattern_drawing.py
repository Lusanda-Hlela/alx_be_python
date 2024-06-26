# Drawing Patterns with Nested Loops

rows = int(input("Enter the size of the pattern: "))

columns = rows

while rows > 0:
  for i in range(rows):
    for j in range(columns):
      print("*", end="")
    if rows != 0:
      rows -=1
      print()
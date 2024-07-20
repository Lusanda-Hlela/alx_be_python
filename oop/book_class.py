'''
Using the four python class magic methods
1. Construct0r (__init__)
2. Destructor (__del__)
3. String Representation (__str__)
4. Official Representation (__repr__)
'''

class Book:
  # Constructor: Initializes the object with a book title, an author and the publication year.
  def __init__(self, title, author, year):
    self.title = title # String: Title of the book
    self.author = author # String: Author of the book
    self.year = year # Integer: The publication year of the book
    '''
    This is for example purposes only
    '''
   # print(f'Book {str(self.title)} by {str(self.author)} was published  in {int(self.year)}.')
  
  # Destructor: Called when the object is about to be destroyed
  def __del__(self):
    '''This function deletes the object'''
    print(f'Deleting {str(self.title)}')
  
  # String Representation: Used by the str() function and prints statements
  def __str__(self):
    '''Return the book details'''
    return f'{str(self.title)} by {str(self.author)}, published in {int(self.year)}'
  
  # Official Representation: Used by the repr() function and in the interactive interpreter
  def __repr__(self):
    '''Returns a string that recreates the Book instance or Object'''
    return f"Book('{str(self.title)}', '{str(self.author)}', {str(self.year)})"

'''
# Create an object to test with
book1 = Book("Earthquakes", "George Orwell", 1984)


print(str(book1))
print(repr(book1))
del book1
'''
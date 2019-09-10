"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open("foo.txt") as f:
    read_data = f.read()
    print(read_data)
f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

b = open("bar.txt", w+)

b.write("You've heard of any of the so-called 'fathers,'but there's a 'mother of the Internet'? \n")
b.write("'Mother of the Internet.' is Radia Perlman, a network engineer and software designer with a Ph.D. in computer science from MIT\n")
b.write(" She made numerous contributions to the Internet as we know it, holding more than 80 related patents\n")

b.close()

with open("bar.txt") as b:
    read_data = b.read()
    print(read_data)

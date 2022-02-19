#There is a function we are providing in for you in this problem called square. 
#It takes one integer and returns the square of that integer value. 
#Write code to assign a variable called xyz the value 5*5 (five squared). 
#Use the square function, rather than just multiplying with *.

def square(x):
    x = x * x 
    return x 
y = int(input(''))
xyz = int(square(y))


rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

# Write your code here!
num_chars = len(rv)
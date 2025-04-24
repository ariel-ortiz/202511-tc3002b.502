from delta import Compiler


source = '''
    // A line comment.

    0

    /*
    A block
    comment.
    */
'''

c = Compiler('program')
c.realize(source)
print(c.result)

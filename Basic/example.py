#Multi-Line statements
#This is a long comment
#and it extends
#to multiple lines

"""This is also 
a an example of
multi-line comments"""

def multi_line():

    """ DOC STRING FOR multi_line"""

    a = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        7 + 8 + 9

    b = (1 + 2 + 3 +
        4 + 5 + 6 +
        7 + 8 + 9)

    c = ['a',
        'blue',
        'c']

    print (a,b,c)    

    print (multi_line.__doc__)

#Multi Statements in a Single Line

def multi_statement():

    """ DOC STRING FOR multi_statement"""

    ab = 1; bc = 1 ; ac = 1

    print (ab,bc,ac)

    print (multi_statement.__doc__)

def multivalue_multivar():
    
    """DOC STRING FOR multivalue_multivar"""

    d , e, f = 10, 20, 30

    print(d,e,f)

    print (multivalue_multivar.__doc__)


multi_line()

multi_statement()

multivalue_multivar()
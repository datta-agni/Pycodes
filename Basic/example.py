#Multi-Line statements
#This is a long comment
#and it extends
#to multiple lines

"""This is also 
a an example of
multi-line comments"""

def multi_line():

    """ USAGE OF MULTILINE """

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

    """ ASSINGING MULTIPLE VALUE TO MULTIPLE VARIABLES IN A SINGLE LINE """

    ab = 1; bc = 1 ; ac = 1

    print (ab,bc,ac)

    print (multi_statement.__doc__)

def multivalue_multivar():

    """ASSINGING MULTIPLE VALUE TO MULTIPLE VARIABLES IN A SINGLE LINE AT ONCE """

    d , e, f = 10, 20, 30

    print(d,e,f)

    print (multivalue_multivar.__doc__)

def literals():
    a = 0b1010 #Binary Literals
    b = 100 #Decimal Literal 
    c = 0o310 #Octal Literal
    d = 0x12c #Hexadecimal Literal

    #Float Literal
    float_1 = 10.5 
    float_2 = 1.5e2

    #Complex Literal 
    x = 3.14j

    #Charecter Type
    strings = "This si a string"
    char = "ABCD"
    multiline_str = """This is a multiline string with more than one line code."""
    unicode = u"\u00dcnic\u00f6de"
    raw_str = r"raw \n string"

    #Boolean Literal
    x = (1 == True)
    y = (1 == False)
    a = True + 5
    b = False + 50

multi_line()

multi_statement()

multivalue_multivar()
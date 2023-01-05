import math

def is_multiple_of_4(n):
    if n % 4 == 0 or n == 0:
        return True
    else:
        return False
    """Return True if n is a multiple of 4; False otherwise."""

def last_prime(m):
    print(m)
    for i in range(m, 1, -1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
            else:
                prime = True
        if prime == True:
            return i    
"""Return the largest prime number p that is less than or equal to m.
You might wish to define a helper function for this.
You may assume m is a positive integer."""

def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    if b**2 - 4*a*c < 0:
        return "complex"
    else:
        root = ((-b + (b**2 - 4*a*c)**0.5)/(2*a), (-b - (b**2 - 4*a*c)**0.5)/(2*a))
        return root

def new_quadratic_function(a, b, c):

    return lambda x: a*x**2 + b*x + c
 
    """Create and return a new, anonymous function (for example
    using a lambda expression) that takes one argument x and 
    returns the value of ax^2 + bx + c."""

def perfect_shuffle(even_list):
    split1 = even_list[0:int(len(even_list)/2)]
    split2 = even_list[int(len(even_list)/2):]
    new_list = []
    for i in range(len(split1)):
        new_list.append(split1[i])
        new_list.append(split2[i])
    return new_list

    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    Perfect shuffle means splitting a list into two halves and then interleaving
    them. For example, the perfect shuffle of [0, 1, 2, 3, 4, 5, 6, 7] is
    [0, 4, 1, 5, 2, 6, 3, 7]."""


def list_of_3_times_elts_plus_1(input_list):
    return[x*3 +1 for x in input_list]

"""Assume a list of numbers is input. Using a list comprehension,
return a new list in which each input element has been multiplied
by 3 and had 1 added to it."""

def quadruple_vowels(text):
    vowels = 'aeiou'
    new_text = ''
    for char in text:
        if char.lower() in vowels:
            new_text += char * 4
        else:
            new_text += char
    return new_text

    """Return a new version of text, with all the vowels quadrupled.
    For example:  "The *BIG BAD* wolf!" => "Theeee "BIIIIG BAAAAD* woooolf!".
    For this exercise assume the vowels are
    the characters A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""

def count_words(text):
    wordDict = {}
    text = text.lower()
    remove = '.,;!?&()[]{}|:_\\=>"\n`^'

    for char in text:
        if char in remove:
            text = text.replace(char, ' ')

    x = text.split()

    for i in range(len(x)):
        wordDict[x[i]] = x.count(x[i].lower())

    return(wordDict)
      
"""Return a dictionary having the words in the text as keys,
and the numbers of occurrences of the words as values.
Assume a word is a substring of letters and digits and the characters
'-', '+', *', '/', '@', '#', '%', and "'" separated by whitespace,
newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ] { } | : ).
Convert all the letters to lower-case before the counting."""

class Polygon:
    def __init__(self, n_sides,lengths=None, angles=None):

        if n_sides == 3 and lengths != None and angles == None:
            angles = []
            angles.append(math.degrees(math.acos((lengths[0]**2 + lengths[1]**2 - lengths[2]**2) / (2 * lengths[0] * lengths[1]))))
            angles.append(math.degrees(math.acos((lengths[0]**2 + lengths[2]**2 - lengths[1]**2) / (2 * lengths[0] * lengths[2]))))
            angles.append(math.degrees(math.acos((lengths[1]**2 + lengths[2]**2 - lengths[0]**2) / (2 * lengths[1] * lengths[2]))))

        self.n_sides = n_sides
        self.lengths = lengths
        self.angles = angles

    def is_rectangle(self):
        if self.n_sides == 4:
            if self.angles != None:
                if self.angles == [90.0, 90.0, 90.0, 90.0]:
                    return True
                else:
                    return False
            else :
                return None
        else:
            return False

    def is_rhombus(self):
        if self.n_sides == 4:
            if self.lengths != None:
                if all(i == self.lengths[0] for i in self.lengths):
                    if self.angles != None:
                        if self.angles[0] == self.angles[2]:
                            return True
                        else:
                            return False
                    else :
                        return None
                else:
                    return False
            else:
                return None
        else:
            return False

    def is_square(self):

        if self.is_rectangle() == True:
            if (self.lengths != None):
                if all(i == self.lengths[0] for i in self.lengths):
                    return True
            else:
                return None
        elif (self.is_rectangle() == None): 
            return None
        else:
            return False
            #[90.0, 90.0, 90.0, 90.0] + is_rectangle

    def is_regular_hexagon(self):
        if self.n_sides == 6:
            if all(i == self.lengths[0] for i in self.lengths):
                if self.angles != None:
                    if self.angles == [120.0, 120.0, 120.0, 120.0, 120.0, 120.0]:
                        return True
                    else:
                        return False
                else :
                    return None
            else:
                return False
        else:
            return False
   
    def is_isosceles_triangle(self):
        if (self.is_triangle() == True):
            if (self.angles != None):
                if (self.angles[0] == self.angles[1] or self.angles[0] == self.angles[2] 
                or self.angles[1] == self.angles[2] and self.is_equilateral_triangle() == False):
                    return True
                else:
                    return False
            else :
                return None
        pass

    def is_equilateral_triangle(self):
        if (self.is_triangle() == True):
            if (self.angles != None):
                if (all(i == self.angles[0] for i in self.angles)):
                    return True
                else:
                    return False
            else :
                return None
        else:
            return False

    def is_scalene_triangle(self):
        if (self.is_triangle() == True):
            if (self.angles != None):
                if (self.angles[0] != self.angles[1] and self.angles[0] != self.angles[2] 
                and self.angles[1] != self.angles[2]):
                    return True
                else:
                    return False
            else :
                return None

    def is_triangle(self):
        if (self.n_sides == 3):
            return True
        else:
            return False

"""Polygon class.  See the spec web page for details."""
""" returns True if the polygon is a rectangle,
False if it is definitely not a rectangle, and None
if the angle list is unknown (None)."""

my_tri = Polygon(3)
print(my_tri.is_equilateral_triangle())
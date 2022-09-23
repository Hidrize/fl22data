"""
    cs260-fl22-a1 programming assignment
    Name: <your name>

    The README file is provided here: 
    https://github.com/bfilin/fl22data/blob/main/programming/a1/README

"""

from string import hexdigits

class Nums:
    def __init__(self, num = None, base = None,
                 new_base = None, debug = False):
        """Constructor for our Nums class, do not modify this method!"""

        if not isinstance(num, str):
            raise TypeError('The num must be a given as str.')

        if not isinstance(base, str):
            raise TypeError('The base must be given as str.')

        if not isinstance(new_base, str):
            raise TypeError('The new_base must be given as str.')

        _valid_bases = ('2', '8', '10', '16')
        if base not in _valid_bases:
            raise ValueError('base value ' 
                             + base + ' is not valid.' 
                             + ' base must be one of the following: '
                             + '"2", "8", "10" or "16"')

        if new_base not in _valid_bases:
            raise ValueError('new_base value ' 
                             + new_base + 'is not valid.'
                             + 'must be one of the following:'
                             + '"2", "8", "10" or "16"')

        if not all([emt in hexdigits[:int(base)] for emt in num.lower()]):
            raise ValueError('Invalid digits in num found. Valid digits for', 
                             base,'are', hexdigits[:int(base)])

        # instance variables
        self.num = num.lower()
        self.base = base
        self.new_base = new_base
        self.debug = debug
        # lookup_table1 can be used with your weighted_sum implementation 
        self.lookup_table1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                              'a': 10, 'b': 11, 'c': 12, 'd': 13,
                              'e': 14, 'f': 15} 
        # lookup_table2 can be used with your repeated_division implementation 
        self.lookup_table2 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                              5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                              10: 'a', 11: 'b', 12: 'c', 13: 'd',
                              14: 'e', 15: 'f'}
        '''
        Note: The above definitions of lookup tables is equivalent to the following:
        self.lookup_table1 = {x:hexdigits[:16].index(x) for x in hexdigits[:16]}
        self.lookup_table2 = {hexdigits[:16].index(x):x for x in hexdigits[:16]}
        '''

        print(self.__class__.__name__, 'object created.',
              'num:', self.num + ',',
              'base:', self.base + ',',
              'new_base:', self.new_base)

    def __repr__(self):
        """Defines string representation for obj

        When we use print(obj) it will print the
        out string from this method.
        """
        pass

    def repeated_division(self):
        """Converts the decimal number num to a new_base representation.

        The repeated division algorithm divides the decimal number by new_base, 
        after each division the remainder is recorded in a collection(e.g. str)
        division is performed until a quotient of zero is obtained.

        The final answer is the collection of all of the remainders
        such that first remainder is the Least Significant Digit (LSD), and the
        last remainder that was obtained is the Most Significant Digit (MSD)
        Note: you can use lookup_table2 with your implementation.
        """
        pass

    def weighted_sum(self):
        """Converts the number num to a decimal representation.

        The weighted sum algorithm converts number that is given
        in either octal, binary or hexadecimal to a decimal representation. 
        Each digit of the number is multiplied by the weight=base^exp

            Σ(d_i * base^(n-i))  where n = len(num) - 1, 0<= i <= n

        If the number is already decimal returns the number unchanged.
        Note: you can use lookup_table1 with your implementation.
        """
        pass


    def number_converter(self):
        """Decides how conversion should be performed and calls helper methods.

        Inspects the num, base, new_base instance variables and
        decides which corresponding convert helper methods should be called.
        The return value from convert method is returned by this method.
        For the assignment the convert helper methods are:
            weighted_sum()
            repeated_division()
        """
        pass

    def get_number(self):
        """Returns the value of the num instance variable."""
        pass

    def get_number_base(self):
        """Returns the value of the base instance variable."""
        pass

    def get_new_base(self):
        """Returns the value of the new_base instance variable."""
        pass

    def set_number(self, num, base):
        """Updates num, base instance variables with parameter values."""
        pass

    def set_new_base(self, new_base):
        """Updates the new_base instance variable with parameter value."""
        pass

if __name__ == '__main__':
    num = '1011'
    base = '2'
    new_base = '10'
    obj1 = Nums(num = '1011', base = '2', new_base = '10')
    ''' 
        Make sure to implement and test all of your your methods.
        Any method that currently has pass keyword in the body should
        be implemented and tested.

        For example: 
            after you finish implementation of get_number() method
            make sure to test it by calling it after instantiation of
            the obj1:
            print('get_number() ',  obj1.get_number())

    '''
 
    

"""
    cs260-fl22-a1 programming assignment
    Name: <your name>

The starter code is provided here and is already include below:
https://github.com/bfilin/fl22data/blob/main/programming/a1/cs260_fl22_a1.py

Video overview for assignment a1:
https://youtu.be/VDSD0UWL1RA

Video pushing from Repl to GitHub:
https://youtu.be/CM0ria1Kf7Q

"""

from string import hexdigits

class Nums:
    def __init__(self, num = None, base = None,
                 new_base = None, debug = False):
        """Constructor for our Nums class, do not modify this method!

        Parameters:
             num -- number, e.g. '1011' 
                    (default None, expected to be a string)

            base -- describes the current base of num, e.g. '2' 
                    (default None, expected to be a string)

        new_base -- describes the new desired base for num, e.g. '10'
                    (default None, expecte to be a string)

           debug -- not used in this implementation
        """

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
            raise ValueError('Invalid digits in num found. Valid digits for base', 
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
        """Converts the decimal number self.num to a self.new_base representation.

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
        """Converts the number self.num to a decimal representation.

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
    """Guard the code from needless execution, if our file is use as module.

    Make sure to test your implementation of your methods here.
    For example:
        After you finish implementation of get_number() method
        make sure to test it by calling:
        print('get_number() ',  obj1.get_number())
    """
    num = '1011'
    base = '2' # 0 1
    new_base = '10'
    obj1 = Nums(num, base, new_base)
    print('get_number() ',  obj1.get_number())
    '''
    write your tests for other methods above this multiline comment
    
    Examples for possible test cases:
    # convert binary base 2 number 1011 to decimal base 10
    obj1 = Nums(num = '1011', base = '2', new_base = '10') 
    obj1.weighted_sum() --> '11'      # returns decimal number 11
    obj1.number_converter() --> '11'  # returns decimal number 11
    obj1.repeated_division() --> None # returns None, since we are converting from bin->dec

    # convert octal base 8 number 1011 to decimal base 10
    obj2 = Nums(num = '1011', base = '8', new_base = '10') 
    obj2.weighted_sum() --> '521'     # returns decimal number 521
    obj2.number_converter() --> '521' # returns decimal number 521
    obj2.repeated_division() --> None # returns None, since we are converting from oct->dec

    # convert hexadecimal base 16 number 1011 to decimal base 10
    obj3 = Nums(num = '1011', base = '16', new_base = '10') 
    obj3.weighted_sum() --> '4113'    # returns decimal number 4113
    obj3.number_converter() --> '4113'# returns decimal number 4113
    obj3.repeated_division() --> None # returns None, since we are converting from hex->dec

    # convert base 10 number 244 to binary base 2
    obj4 = Nums(num = '244', base = '10', new_base = '2') 
    obj4.repeated_division() --> '11110100' # returns binary number 11110100
    obj4.number_converter() --> '11110100'  # returns binary number 11110100
    obj4.weighted_sum() --> None            # returns None, since we are converting from dec->bin

    # convert base 10 number 244 to octal base 8
    obj5 = Nums(num = '244', base = '10', new_base = '8') 
    obj5.repeated_division() --> '364' # returns octal number 364
    obj5.number_converter() --> '364'  # returns octal number 364
    obj5.weighted_sum() --> None       # returns None, since we are converting from dec->oct

    # convert base 10 number 244 to hexadecimal base 16
    obj6 = Nums(num = '244', base = '10', new_base = '16') 
    obj6.repeated_division() --> 'f4'  # returns hexadecimal number f4
    obj6.number_converter() --> 'f4'   # returns hexadecimal number f4
    obj6.weighted_sum() --> None       # returns None, since we are converting from dec->hex

    '''
   

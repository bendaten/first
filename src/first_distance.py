class FirstDistance(object):

    @staticmethod
    def is_valid_unit(unit):

        """
        Check if a string is one of the known length units

        :param unit: a unit string to check
        :type unit: str
        :return: True if unit is one of the recognized length unit strings
        :rtype: bool
        """
        return unit in ['m', 'km', 'ft', 'mile']

    conversions = {'m': 1, 'km': 1000, 'mile': 1609.344, 'ft': 0.3048}

    def __init__(self, distance, unit):

        """
        Constructor

        :param distance: positive distance value
        :type distance: float
        :param unit: length unit
        :type unit: str
        :return: instance of FirstDistance
        :rtype: FirstDistance
        """
        if distance < 0:
            raise ValueError('FirstDistance.__init__ - %1s is not a positive number' % distance)
        self.distance = distance

        if not self.is_valid_unit(unit):
            raise ValueError('FirstDistance.__init__ - "%1s" is not a valid unit' % unit)
        self.unit = unit

    @classmethod
    def from_string(cls, string):

        """
        Instantiate FirstDistance from a string input

        :param string: a distance with value and unit like '4.5 km'
        :type string: str
        :return: instance of FirstDistance created from the string
        :rtype: FirstDistance
        """

        tokens = string.split()
        if len(tokens) != 2:
            raise ValueError('FirstDistance.from_string - from_string() ' +
                             'expects 2 tokens, number and unit, but got "%1s"' % string)

        try:
            value = float(tokens[0])
        except ValueError as ex:
            raise ValueError('FirstDistance.from_string - from_string() ' +
                             'exprects the first token to be a number but ' + str(ex))
        unit = tokens[1]

        return cls(value, unit)

    def __str__(self):

        return str(self.distance) + ' ' + self.unit

    def convert_to(self, unit):

        """
        Convert a distance value to another unit

        :param unit: to unit
        :type unit: str
        :return: the converted value
        :rtype: float
        """

        if not self.is_valid_unit(unit):
            raise ValueError('FirstDistance.convert_to - %1s is not a valid unit' % unit)

        if self.unit == unit:
            return self.distance
        else:
            to_m = self.conversions[self.unit]
            from_m = self.conversions[unit]
            return self.distance * to_m / from_m

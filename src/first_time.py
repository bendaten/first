from datetime import timedelta
from dateutil.parser import parse


class FirstTime(timedelta):

    def __init__(self, hours=0, minutes=0, seconds=0):

        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError(self.__class__.__name__ + ' does not allow negative values')

        super(FirstTime, self).__init__(hours=hours, minutes=minutes, seconds=seconds)
        # super(FirstTime, self).__init__()

    conversions = {'second': 1, 'minute': 60, 'hour': 3600}

    @classmethod
    def from_string(cls, string):

        """
        Create FirstTime from a string
        
        :type string: str
        :param string: format - HH:MM:SS
        :return: instance of FirstTime
        :rtype: FirstTime
        """
        try:
            t_from_str = parse(string)
        except ValueError as ex:
            raise ValueError(str(ex) + ' - "' + string + '"')

        if t_from_str.hour == 0 and t_from_str.minute == 0 and t_from_str.second == 0:
            raise ValueError('unknown string format for "%1s"' % string)

        return cls(hours=t_from_str.hour, minutes=t_from_str.minute, seconds=t_from_str.second)

    def convert_to(self, unit):

        """
        Convert a duration value to another unit

        :param unit: to unit
        :type unit: str
        :return: the converted value
        :rtype: float
        """

        if unit not in self.conversions:
            raise ValueError('%1s is not a valid unit' % unit)

        seconds = super(FirstTime, self).total_seconds()

        if unit == 'second':
            return seconds
        else:
            return seconds / self.conversions[unit]

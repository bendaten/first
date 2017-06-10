from datetime import timedelta

from first_time import FirstTime
from first_distance import FirstDistance


class FirstPace(object):

    def __init__(self, minutes=0, seconds=0, length_unit='mile'):

        if not FirstDistance.is_valid_unit(length_unit):
            raise ValueError('FirstPace: "%1s" is not a valid length unit' % length_unit)
        self.time = FirstTime(minutes=minutes, seconds=seconds)
        self.length_unit = length_unit

    def __str__(self):

        return str(self.time) + ' min per ' + self.length_unit

    @classmethod
    def from_string(cls, str_input):

        """
        Instantiate FirstPace from a string input
        
        :param str_input: format - '0:MM:SS per unit'
        :type str_input: str
        :return: instance of FirstPace
        :rtype: FirstPace
        """
        tokens = str_input.split()

        p_time = FirstTime.from_string(tokens[0])  # pass the exception on
        length_unit = tokens[-1]

        if not FirstDistance.is_valid_unit(tokens[-1]):
            raise ValueError('FirstPace: "%1s" is not a valid length unit' % length_unit)

        return cls(p_time.seconds//60, p_time.seconds % 60, length_unit)

    def to_time(self, distance, unit):

        """
        How much time will take to run a given distance with this pace
        
        :type distance: FirstDistance
        :param distance: the distance
        :param unit: the desired unit of the result
        :return: the time value for this unit
        :rtype: float
        """
        factor = distance.convert_to(self.length_unit)
        seconds = self.time.total_seconds() * factor
        result_time = FirstTime(seconds=seconds)
        return result_time.convert_to(unit)

    def to_distance(self, time, unit):

        """
        How far you run given duration with this pace
        
        :param time: the duration
        :param unit: the desired unit of the result
        :return: the distance value for this unit
        :rtype: float
        """
        factor = time.total_seconds()/self.time.total_seconds()
        result_distance = FirstDistance(factor, self.length_unit)
        return result_distance.convert_to(unit)

    @classmethod
    def from_time_distance(cls, time, distance, unit=None):

        if unit is None:
            unit = distance.unit
        factor = distance.convert_to(unit)  # 400m with unit = mile will become ~0.25
        seconds = time.total_seconds() / factor  # 2 minutes for 400m will give ~(2*60)/0.25

        return cls(minutes=seconds//60, seconds=round(seconds % 60), length_unit=unit)

    def increment(self, seconds):

        self.time += timedelta(seconds=seconds)

    def meters_per_second_delta(self, delta_in_seconds):

        if not isinstance(delta_in_seconds, int):
            raise ValueError('FirstPace.meters_per_second_delta - delta_in_seconds must be an integer')

        seconds = self.time.total_seconds() + delta_in_seconds
        meters = FirstDistance(distance=1.0, unit=self.length_unit).convert_to(unit='m')

        return meters / seconds

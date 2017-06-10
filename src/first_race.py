import datetime

from first_distance import FirstDistance
from first_pace import FirstPace
from first_time import FirstTime


class FirstRaceType(object):

    def __init__(self, name, distance, unit):

        if not FirstDistance.is_valid_unit(unit):
            raise ValueError('FirstRace: "%1s" is not a valid length unit' % unit)
        self.name = name
        self.distance = FirstDistance(distance=distance, unit=unit)

    def __str__(self):

        return self.name + ' - ' + str(self.distance)


class FirstRace(object):

    # noinspection PyTypeChecker
    def __init__(self, race_type, name, race_date, target_time=None):

        if not isinstance(race_type, FirstRaceType):
            raise TypeError('race type must be an instance of FirstRaceType')
        if not isinstance(name, basestring):
            raise TypeError('name must be a string')
        if not isinstance(race_date, datetime.date):
            raise TypeError('race_date must be an instance of datetime.date')
        if target_time is not None and not isinstance(target_time, FirstTime):
            raise TypeError('target_time must be an instance of FirstTime')

        self.race_type = race_type
        self.name = name
        self.race_date = race_date
        self.target_time = target_time
        self.status = 'scheduled'
        self.actual_time = None

    statuses = ['scheduled', 'done', 'skipped']

    # noinspection PyTypeChecker
    def set_status(self, status):

        if not isinstance(status, basestring):
            raise TypeError('status must be a string')

        if status in self.statuses:
            self.status = status
        else:
            raise ValueError('Status not in ' + str(self.statuses))

    def __str__(self):

        out_string = (self.name + ' of type ' + str(self.race_type) + '\n' +
                      'On ' + str(self.race_date) + '\n')
        if self.target_time is not None:
            out_string += 'Target time - ' + str(self.target_time) + '\n'
        out_string += 'Status - ' + self.status + '\n'
        if self.status == 'done' and self.actual_time is not None:
            out_string += 'Actual time - ' + str(self.actual_time) + '\n'

        return out_string

    def details(self, level=0, indent=''):

        out_string = indent + 'Race:\n'
        out_string += indent + '  ' + self.name + ' of type ' + str(self.race_type) + '\n'
        if level > 0:
            out_string += indent + '  On ' + str(self.race_date) + '\n'
            if self.target_time is not None:
                out_string += indent + '  Target time - ' + str(self.target_time) + '\n'
            out_string += indent + '  Status - ' + self.status + '\n'
            if self.status == 'done' and self.actual_time is not None:
                out_string += indent + '  Actual time - ' + str(self.actual_time) + '\n'

        return out_string

    def set_target_time(self, a_time=None):

        if a_time is not None and not isinstance(a_time, FirstTime):
            raise TypeError('a_time must be an instance of FirstTime')

        self.target_time = a_time

    def set_actual_time(self, a_time=None):

        if not isinstance(a_time, FirstTime):
            raise TypeError('a_time must be an instance of FirstTime')

        self.actual_time = a_time

    def race_pace(self):

        return FirstPace.from_time_distance(time=self.target_time, distance=self.race_type.distance)

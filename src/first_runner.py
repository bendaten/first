

# noinspection PyTypeChecker
from first_utils import FirstUtils


class FirstRunner(object):

    # noinspection PyTypeChecker
    def __init__(self, name, age=None, gender=None, email=None, length_unit='mile'):

        if not isinstance(name, basestring):
            raise TypeError('FirstRunner.__init__ - name must be a string')
        if age is not None:
            if not isinstance(age, int):
                raise TypeError('FirstRunner.__init__ - age must be an integer')
            if age <= 0:
                raise ValueError('FirstRunner.__init__ - age must be positive')
        if gender is not None:
            if not isinstance(gender, basestring):
                raise TypeError('FirstRunner.__init__ - gender must be a string')
            # for now no limit on gender but if the plan has gender related instructions then we might post a warning
            # when a gender is not recognized by the plan
        if not isinstance(length_unit, basestring):
            raise TypeError('FirstRunner.__init__ - length_unit is expected to be a string')

        if FirstUtils.is_internet_on():
            from validate_email import validate_email

            if email is not None and not validate_email(email):
                raise ValueError('FirstRunner.__init__ - invalide email address')

        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.length_unit = length_unit

    def __str__(self):

        out_string = 'Name - ' + self.name + '\n'
        if self.age is not None:
            out_string += 'Age - ' + str(self.age) + '\n'
        if self.gender is not None:
            out_string += 'Gender - ' + self.gender + '\n'
        if self.email is not None:
            out_string += 'Email - ' + self.email + '\n'

        return out_string

    def details(self, level=0, indent=''):

        out_string = indent + 'Runner:\n'
        out_string += indent + '  Name - ' + self.name + '\n'
        if level > 0:
            if self.age is not None:
                out_string += indent + '  Age - ' + str(self.age) + '\n'
            if self.gender is not None:
                out_string += indent + '  Gender - ' + self.gender + '\n'
            if self.email is not None:
                out_string += indent + '  Email - ' + self.email + '\n'

        return out_string

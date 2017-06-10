from os.path import expanduser

from first_data import FirstData
from first_distance import FirstDistance
from first_pace import FirstPace
from first_step import FirstStepBody
from first_time import FirstTime


def main():

    pace1 = FirstPace.from_string('0:10:00 min per mile')
    step1 = FirstStepBody(step_id=13, name='bla', pace=pace1, distance=FirstDistance.from_string('1000 m'))
    print step1

    step2 = FirstStepBody(step_id=11, name='bli', pace=pace1, time=FirstTime.from_string('0:10:00'))
    print step2

    FirstStepBody.reset_global_id()
    step3 = FirstStepBody(step_id=4, name='blu', pace=pace1, distance=FirstDistance.from_string('10 km'))

    print step3


# ----------------------------------------------------------
if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

import json
import datetime
import random
import sys
import time
from operator import itemgetter
from storage import insert_exercise
from make_sound import play_finished, play_intermission

# set to true if you don't want the exercises to actually wait  - 1 second elapse
testing = False


keys = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# the params will come from user input
params = json.loads('{"timeSig":"4/4","key":"random","mode":"random"}')


def reorder(note):
    return keys[keys.index(note):] + keys[:keys.index(note)]


def rearrange_indices(mode):
    temp_mode = mode[1:] + [12]
    new_mode = list(map(lambda x: x - temp_mode[0], temp_mode))
    return new_mode


with open('modes.json') as mode_file:
    modes = json.load(mode_file)

today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1

# use day of year to make seed - that way you can come back to it if you need to
random.seed(day_of_year)


def make_sequences(params):
    params['date'] = today.strftime("%m/%d/%Y")
    params['seed'] = day_of_year
    if params['key'] == 'random':
        params['key'] = random.choice(keys)

    if params['mode'] == 'random':
        params['mode'] = random.choice(list(modes.items()))

    # 1 make scales
    scale = itemgetter(*params['mode'][1])(reorder(params['key']))

    # 2 make triads
    # note you need to add the inverstions too
    triads, chords = [], []

    for scale_degree, note in enumerate(scale):

        if scale_degree == 0:
            chords.append(itemgetter(*[0, 2, 4, 6])(scale))
            triads.append(itemgetter(*[0, 2, 4])(scale))
            mode_indices = params['mode'][1]

        else:
            mode_indices = rearrange_indices(mode_indices)
            current_mode = itemgetter(*mode_indices)(reorder(note))

            chords.append(itemgetter(*[0, 2, 4, 6])(current_mode))
            triads.append(itemgetter(*[0, 2, 4])(current_mode))

    return {'params': params, 'scales': scale, 'chords': chords, 'triads': triads}


def perform_exercise(duration, testing=testing):
    # make system sound when done after seconds
    sleeptime = 1 if testing else 60

    for minute in list(range(1, int(duration)+1)):
        print('          Minute %s / %s' % (minute, round(duration)))
        time.sleep(sleeptime)
    print()

    return duration


def schedule():
    data = make_sequences(params)

    with open('exercises.json') as json_file:
        instrument_exercises = json.load(json_file)
    for ex_list in instrument_exercises:
        print('     ********************')
        print('     Instrument is %s' % ex_list)
        for exercise in instrument_exercises[ex_list]:
            if exercise == 'scales':
                print("               Practice %s - %s" %
                      (params['mode'][0], ', '.join(data[exercise])))

                perform_exercise(instrument_exercises[ex_list][exercise])

            elif exercise != 'chords' and exercise != 'triads':
                print("               Practice %s" % (exercise))

                perform_exercise(instrument_exercises[ex_list][exercise])

            else:
                time_division = instrument_exercises[ex_list][exercise]/len(
                    data[exercise])
                for interval in data[exercise]:
                    print("               Current %s to practice is %s" %
                          (exercise, ', '.join(interval)))
                    perform_exercise(time_division)
                    play_intermission()

            # print(exercise, instrument_exercises[ex_list][exercise], ex_list)

            if not testing:
                insert_exercise(
                    exercise, instrument_exercises[ex_list][exercise], ex_list)

            play_finished()
            keep_going = input('     Any key to continue, or hit x to quit')
            if keep_going.lower() == 'x':
                break
    return


if __name__ == "__main__":
    schedule()

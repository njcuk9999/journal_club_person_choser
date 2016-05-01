"""
Program to decide who presents at journal club
"""
import random
import numpy as np

# Journal Club Attendees
# 0 = presented last week
# 1 = default weighting
# 2 = no show last week
# 2*n = multiplier for n number of weeks no show
people = dict(Bob=1,
              Richard=0,
              Judy=1,
              Alice=1,
              Fred=4,
              John=1,
              Mike=2)


def create_weighted_list(peoplex, no_showx):
    """
    Function to create a list using weights (avoiding no shows)
    :param peoplex:
    :param no_showx:
    :return:
    """
    jc_listx = []
    for name in peoplex:
        if peoplex[name] == 0:
            continue
        if peoplex[name] in no_showx:
            continue
        else:
            jc_listx += [name] * peoplex[name]
    return jc_listx


def run_jc(display=True):
    """
    Runs the journal club selector a single time
    :param display:
    :return:
    """
    #Define No shows
    no_show = [None]

    jc_list = create_weighted_list(people, no_show)
    selected_person = random.sample(jc_list, 1)[0]

    #print the name of the lucky person
    if display:
        print "\n" + "=" * 50
        print "\n" + "\t Journal Club Presenter Selector"
        print "\n" + "-" * 50
        print '\n' + '\t The winner is: {0}'.format(selected_person)
        print "\n" + "=" * 50

    return selected_person


def run_multi_jc(N=1001):
    """
    Runs the journal club selector N times
    :param N:
    :return:
    """
    d = dict()
    for n in range(N):
        selected_n = run_jc(display=False)
        if selected_n not in d:
            d[selected_n] = 1
        else:
            d[selected_n] += 1

    #sort by num
    names, values = np.array(d.keys()), np.array(d.values())
    mask = np.argsort(values)[::-1]
    names, values = names[mask], values[mask]

    print "\n" + "=" * 50
    print "\n" + "\t Journal Club Presenter Selector"
    print "\n" + "-" * 50
    for n in range(len(names)):
        name, value = names[n], values[n]
        print '\n' + '\t' + ' {0} was selected {1} times'.format(name, value)
    print "\n" + "=" * 50


if __name__ == '__main__':
    run_jc()

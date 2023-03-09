#!/usr/bin/python3
from typing import Any, List

def SatbleMatch(preference_hospital: List[List[int]], 
                preference_student: List[List[int]]) -> Any:
    '''
    The hospitals and students are numbered  from 0 to n - 1.
    We just simulate the Gale-Shapley algorithm,
    and all operation happend on list with O(1),
    so the upper bound of run time is n^2.
    '''
    # the number of hospitals (students)
    n = len(preference_hospital)
    # a list of mapping from hospital to its order in a student's preference
    # in the form of list
    h2idx = [[0] * n for _ in range(n)]
    for s in range(n):  # traverse students
        for idx in range(n):  # traverse student's preference
            h2idx[s][preference_student[s][idx]] = idx  # set mapping
    # a mapping from student to the hospital he has been matched
    # in the form of list
    res = [-1] * n
    # a list to store hospitals which still have no students
    hospitals = list(range(n))
    # a list to record the index (preference order) 
    # of the next student a hospital should send an offer
    last_offer = [0] * n

    # if there are still some hospitals which have no students
    while hospitals:
        h = hospitals.pop()  # traverse these hospital
        matched = False  # init the state as not matched
        # as the current hospital is not matched, 
        # we should keep on finding by the order of its preference list
        while not matched:
            # next student the hospital should send offer to
            next_student = preference_hospital[h][last_offer[h]]
            # when this student is not matched
            if res[next_student] == -1:
                res[next_student] = h
                matched = True
            # when the student is matched but he like h a bit more
            elif h2idx[next_student][res[next_student]] > h2idx[next_student][h]:
                hospitals.append(res[next_student])
                res[next_student] = h
                matched = True
            last_offer[h] += 1
    # return all pairs as a list of tuple
    return [(h, s) for s, h in enumerate(res)]


ph = [[0, 1, 2], [1, 0, 2], [0, 1, 2]]
ps = [[1, 0, 2], [0, 1, 2], [0, 1, 2]]
print(SatbleMatch(ph, ps))

def min_lecture_rooms(lecture_times):

    # print(lecture_times)
    lst = []
    for lec in lecture_times:
        lst.append(lec[0])
        lst.append(lec[1])

    # print(lst)

    min_rooms = 0
    for minute in range(min(lst),max(lst)):
        # print('Minute: %s' % minute)
        lectures_running = 0
        for lecture in lecture_times:
            if lecture[0] < minute < lecture[1]:
                lectures_running += 1
        # print(lectures_running)

        if min_rooms < lectures_running:
            min_rooms = lectures_running

    return min_rooms



min_lecture_rooms([(30, 75), (150, 160), (80, 170),(40,130)])

min_lecture_rooms([(30, 75), (0, 50), (60, 150),(40,130),(140,160),(140,160)])






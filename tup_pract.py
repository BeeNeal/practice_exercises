# def parse_data(filename):
#     """read and split"""

#     file_data = open(filename)
#     for line in file_data:
#         items = line.split('|')


def unique_houses(filename):
    """TODO: Return a set of student houses."""

    house_info = open(filename)
    houses = []
    for line in house_info:
        items = line.split('|')
        houses.append(items[2])
    return set(houses)

# print unique_houses("cohort_data.txt")


def sort_by_cohort(filename):
    """sorting students by cohort"""

    cohort_info = open(filename)
    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    for line in cohort_info:
        items = line.split('|')
        # if items[4] != "I\n":
        #     all_students.append(" ".join(items[0:2]))
        if items[4] == 'Winter 2016\n':
            winter_16.append(" ".join(items[0:2]))
        elif items[4] == 'Spring 2016\n':
            spring_16.append(" ".join(items[0:2]))
        elif items[4] == 'Summer 2016\n':
            summer_16.append(" ".join(items[0:2]))
        elif items[4] == 'Fall 2015\n':
            fall_15.append(" ".join(items[0:2]))
        elif items[4] == 'G\n':
            ghosts.append(" ".join(items[0:2]))

    all_students = winter_16 + spring_16 + summer_16 + fall_15 + ghosts
    return all_students

    #below list comp doesn't work yet
    # winter_16 = [items[0:2] for item in items if items[4] == 'Winter 2016\n']


# below = ghosts works!
    # for line in cohort_info:
    #     items = line.split('|')
    #     if items[4] == "G\n":
    #         ghosts.append(" ".join(items[0:2]))
    # return ghosts



sort_by_cohort("cohort_data.txt")

# problem: program not finding my data file
# solution: make sure it's in the sames directory!


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
    students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    for line in cohort_info:
        items =line.split('|')
        all_students.append(" ".join(items[0:2]))
    return all_students


    return students

sort_by_cohort("cohort_data.txt")

# problem: program not finding my data file
# solution: make sure it's in the sames directory!


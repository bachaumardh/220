"""
Name: Hugo Bachaumard
vigenere.py

Problem: Write a program that practices string data and function development.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    outfile = open(out_file_name, 'w')
    infile = open(in_file_name, 'r')
    contents = infile.readlines()
    class_average = 0
    for i in contents:
        grades = i.strip().split()
        cleaned = [x for x in grades if x.isdigit()]
        average = 0
        total_weight = 0
        for j in range(len(cleaned)//2):
            weight = int(cleaned[j*2])
            grade = int(cleaned[(j*2)+1])
            average = average + (grade * weight)
            total_weight += weight
        average = average / 100
        class_average += average / len(contents)
        names = [name for name in grades if not name.isdigit()]
        names = " ".join(names)
        if total_weight == 100:
            outfile.write(names[:-1] + "'s average: " + str(round(average, 1)) + "\n")
        else:
            if total_weight > 100:
                outfile.write(names[:-1] + "'s average: " + "Error: The weights are more than 100." + "\n")
            if total_weight < 100:
                outfile.write(names[:-1] + "'s average: " + "Error: The weights are less than 100." + "\n")

    outfile.write('Class average: {:.1f}'.format(class_average))


def main():
    weighted_average("grades.txt", "avg.txt")
main()


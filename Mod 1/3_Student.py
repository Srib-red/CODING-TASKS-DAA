import csv

header = ['Name', 'Age', 'Department', 'Grade']
data = [
    ['Alireaiza', 20, 'CS', 'O'],
    ['Micheal', 21, 'IT', 'A'],
    ['Rai', 19, 'AI', 'A+'],
    ['Pothos', 22, 'Math', 'A-'],
    ['Compuait', 23, 'ECE', 'B++'],
    ['Verimaia', 20, 'Mechanical', 'O--'],
    ['Chaar', 21, 'Biotech', 'C++']
]

file1 = open('students.csv', 'w', newline='')
writer = csv.writer(file1)
writer.writerow(header)
writer.writerows(data)
file1.close()

print("students.csv' created.")

"""
Passing dictionary key to find the average of that particular person.
"""

def main(student_marks, query_name):
    # student_marks = {'Harish': [67.0, 68.0, 69.0], 'Jerry': [70.0, 98.0, 63.0]}
    vals = student_marks[f'{query_name}']
    tot = 0
    for val in vals:
        tot += val
    avg = tot / len(vals)
    print(f'{avg:.2f}')
    
if __name__ == '__main__':
    n = int(input("Number of students to check: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input('Enter the name along with marks: ').split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input('Enter the name to search: ')
    main(student_marks, query_name)

"""
Input: 
Number of students to check: 2
Enter the name along with marks: 
Harish 67 68 69
Jerry 100 90 95
Vijayarasan 70 93 63
Enter the name to search: Jerry
"""
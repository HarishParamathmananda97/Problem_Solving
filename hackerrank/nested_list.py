def main(nested_ls):
    sorted_ls = sorted(nested_ls, key = lambda val: val[1])
    # print(sorted_ls)
    first_no = sorted_ls[0][1]
    second_no = first_no
    
    names = []
     
    one_time = True
    for nam in sorted_ls:
        if nam[1] == first_no:
            continue
        if one_time:
            second_no = nam[1]
            one_time = False
        if nam[1] == second_no:
            names.append(nam[0])
    names.sort()
    for name in names: 
        print(name)


if __name__ == '__main__':
    nested_ls = []
    for _ in range(int(input('Enter the number of Students grade: '))):
        name = input('Enter the Name: ')
        score = float(input(f'Enter the {name} grade: '))
        nested_ls.append([name, score])
        
    main(nested_ls)

"""
sampleInput: [['harish', 89.3], ['jerry', 100.4], ['kumar', 95.0], ['mouli', 91.4], ['naveen', 91.4]]
sampleOutput: 
mouli
naveen
"""
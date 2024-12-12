import numpy

def calculate(arr):
    """
    # write a code to convert this array into numpy 3X3
    # mean, variance, standard deviation, max, min, and sum of the rows
    # create a dictionary 
    # dictionary['mean'] = mean.result 
    # print dictionary
    """
    print(arr)


if __name__ == '__main__':
    try:
        num_input = list(map(int, input('Enter the number with space as separator: ').split(' ')))
        if len(num_input) > 9 or len(num_input) < 9:
            raise ValueError('List must contain nine numbers.')
        calculate(num_input)
    except Exception as e:
        print(e)
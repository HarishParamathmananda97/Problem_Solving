def sum_of_even(number=10):
    """
    takes number from user and finds all the even numbers using filter function.
    """

    numbers = [num for num in range(number + 1)]
    # even_no = [num for num in range(number + 1) if num % 2 == 0]
    # print(sum(even_no))
    
    return (sum(filter(lambda no: no % 2 == 0, numbers)))

def main():
    try: 
        print(sum_of_even(int(input("Enter the number: "))))
    except Exception as e: 
        print(f"The error is: {e}")

if __name__ == '__main__':
    main()

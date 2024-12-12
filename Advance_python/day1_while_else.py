def is_comment(item):
    return isinstance(item, str) and item.startswith('#')

def execute(program):
    """Execute a stack program
    Args:
        Program: Any stack-like containing where each item in the stack items on the stack may be strings begining with '#' for the purpose of documentation, stack-like means support for:

        item = stack.pop() # remove and return the top item
        stack.append(item) # push an item to the top
        if stack: # False in a boolean context when empty
    
    """
    # Find the start of the 'program' by skipping
    # Any item which is a comment.
    while program: 
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else: #nobreak
        print("Empty program!")
        return

    # Evaluate the program
    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else: #nobreak
        print("Program successfully.")
        print("Result: ", pending)
    
    print("Finished.")
if __name__ == '__main__':
    print("initiated.")
    import operator
    program = list(reversed((
        "# A short stack program to add", 
        "# and multiply some constants.",
        5,
        2,
        operator.add,
        3,
        operator.mul
    )))
    execute(program)
    print("program ended.")


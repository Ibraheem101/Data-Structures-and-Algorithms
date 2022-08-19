def join(x):
    return "".join(x.lower().split())

def is_palindrome(x):
    # Check if x[0] == x[-1]
    if (len(x) == 1) or (len(x) == 2 and x[0] == x[-1]):
        return True
    if join(x[0]) == join(x[-1]):
        return is_palindrome(join(x[1:-1]))

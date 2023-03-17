import sys

if (len(sys.argv) > 1):
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument are provided")
    else:
        try:
            n = int(sys.argv[1])
            if (n == 0):
                print("I'm Zero.")
            else:
                (print("I'm Even.") if n % 2 == 0 else print("I'm Odd."))
        except Exception:
            print("AssertionError: argument is not an integer")

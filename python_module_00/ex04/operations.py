import sys


def main(A, B):
    print("Sum:\t\t" + str(A + B))
    print("Difference:\t" + str(A - B))
    print("Product:\t" + str(A * B))
    try:
        print("Quotient:\t" + str(A / B))
        print("Remainder:\t" + str(A % B))
    except Exception:
        print(("Quotient:\tERROR (division by zero)"))
        print("Remainder:\tERROR (modulo by zero)")


if __name__ == "__main__":
    n = len(sys.argv)
    if (n > 3):
        print("AssertionError: too many arguments")
    elif (n == 3):
        try:
            A = int(sys.argv[1])
            B = int(sys.argv[2])
            main(A, B)
        except Exception:
            print("AssertionError: only integers")

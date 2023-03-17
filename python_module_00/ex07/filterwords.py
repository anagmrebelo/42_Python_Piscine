import sys
import string

if __name__ == "__main__":
    n = len(sys.argv)
    ponct = string.punctuation

    try:
        if (n == 3 and int(sys.argv[2])):
            temp = sys.argv[1].translate(str.maketrans("", "", ponct))
            temp = temp.split()
            for i in temp:
                if (len(i) < int(sys.argv[2])):
                    temp.remove(i)
            print(temp)
        else:
            print("ERROR")
    except Exception:
        print("ERROR")

import random

def generator(text, sep=" ", option=None): 
    if isinstance(text, str) and (option is None or isinstance(option, str)):
        ret = text.split(sep)
        if (option == None):
            return (ret)
        elif (option == "unique"):
            return list(dict.fromkeys(ret))
        elif (option == "ordered"):
            return sorted(ret)
        elif (option == "shuffle"):
            n = len(ret)
            for i in range(n):
                ret.append(ret.pop(random.randint(0, n-1)))
            return ret
    print("ERROR")
    return []


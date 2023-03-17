import numpy

class TinyStatistician:
    @staticmethod
    def mean(arg):
        list = []
        if arg is None:
            return None
        if isinstance(arg, list):
            list = arg
        else:
            for i in numpy.nditer:
                print(i)
        return 1

if __name__ == "__main__":
    arr = numpy.array([[1, 2, 3], [4, 5, 6]])
    print(TinyStatistician.mean(arr))
    tes = [1, 2, 3 ,4]
    print(TinyStatistician.mean(tes))
import collections.abc

class Vector():
    def __init__(self, arg):
        self.values = []

        # If argument is a list
        if (isinstance(arg, list) and all(isinstance(i, list) for i in arg)):
            # If arg is a row vector
            if (len(arg) == 1 and all(isinstance(arg[0][i], float) for i in range(len(arg[0])))):
                self.shape = (1, len(arg[0]))
                self.values = arg
            # If arg is a column vector
            elif (len(arg) > 1 and all(isinstance(arg[i][0], float) for i in range(len(arg)))):
                    self.shape = (len(arg), 1)
                    self.values = arg
            else:
                raise ValueError("Argument is not valid")
        # If argument is integer
        elif (isinstance(arg, int) and arg > 0):
            for i in range(arg):
                self.values.append([float(i)])
            self.shape = (arg, 1)
        # If argument is tuple
        elif(isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], int) and isinstance(arg[1], int)):
            size = arg[1] - arg[0]
            if (size <= 0):
                raise ValueError("Invalid argument: second number of tuple is smaller than the first one")
            for i in range(arg[0], arg[1]):
                self.values.append([float(i)])
            self.shape = (size, 1)
        else:
            raise ValueError("Argument is not valid")

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        print(self.values)

    def T(self):
        ret = []
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in self.values[0]:
                ret.append([i])
        
        # If arg is a column vector
        else:
            for i in self.values:
                for j in i:
                  ret.append(j)
            ret = [ret]
        return ret

    def dot(self, other):
        ret = 0
        if not isinstance(other, Vector) or other.shape != self.shape:
            raise ValueError("Argument is not valid")
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in range(len(self.values[0])):
                ret += self.values[0][i] * other.values[0][i]
        # If arg is a column vector
        else:
            for i in range(len(self.values)):
                ret += self.values[i][0] * other.values[i][0]
        return ret
           
    def __add__(self, other):
        ret = []
        if not isinstance(other, Vector) or other.shape != self.shape:
             raise ValueError("NotImplementedError")
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in range(len(self.values[0])):
                ret.append(self.values[0][i] + other.values[0][i])
        # If arg is a column vector
        else:
            for i in range(len(self.values)):
                ret.append([self.values[i][0] + other.values[i][0]])
        return ret

    def __radd__(self, other):
        ret = []
        if not isinstance(other, Vector) or other.shape != self.shape:
             raise ValueError("NotImplementedError")
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in range(len(self.values[0])):
                ret.append(other.values[0][i] + sub.values[0][i])
        # If arg is a column vector
        else:
            for i in range(len(self.values)):
                ret.append([other.values[i][0] + self.values[i][0]])
        return ret

    def __sub__(self, other):
        ret = []
        if not isinstance(other, Vector) or other.shape != self.shape:
            raise ValueError("NotImplementedError")
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in range(len(self.values[0])):
                ret.append(self.values[0][i] + other.values[0][i])
        # If arg is a column vector
        else:
            for i in range(len(self.values)):
                ret.append([self.values[i][0] + other.values[i][0]])
        return ret

    def __rsub__(self, other):
        ret = []
        if not isinstance(other, Vector) or other.shape != self.shape:
             raise ValueError("NotImplementedError")
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in range(len(self.values[0])):
                ret.append(other.values[0][i] + self.values[0][i])
        # If arg is a column vector
        else:
            for i in range(len(self.values)):
                ret.append([other.values[i][0] + self.values[i][0]])
        return ret

    def __truediv__(self, other):
        ret = []
        if not isinstance(other, int) and not isinstance(other, float):
             raise ValueError("NotImplementedError")
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in range(len(self.values[0])):
                ret.append(self.values[0][i]/other)
        # If arg is a column vector
        else:
            for i in range(len(self.values)):
                ret.append([self.values[i][0]/other])
        return ret

    def __rtruediv__(self, other):
        ret = []
        raise ValueError("NotImplementedError")
        if not isinstance(other, int) and not isinstance(other, float):
             raise ValueError("NotImplementedError")
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in range(len(self.values[0])):
                ret.append(other/self.values[0][i])
        # If arg is a column vector
        else:
            for i in range(len(self.values)):
                ret.append([other/self.values[i][0]])
        return ret

    def __mul__(self, other):
        ret = []
        if not isinstance(other, int) and not isinstance(other, float):
             raise ValueError("NotImplementedError")
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in range(len(self.values[0])):
                ret.append(self.values[0][i]/other)
        # If arg is a column vector
        else:
            for i in range(len(self.values)):
                ret.append([self.values[i][0]/other])
        return ret

    def __rmul__(self, other):
        ret = []
        if not isinstance(other, int) and not isinstance(other, float):
             raise ValueError("NotImplementedError")
        # If arg is a row vector
        if (len(self.values) == 1):
            for i in range(len(self.values[0])):
                ret.append(other * self.values[0][i])
        # If arg is a column vector
        else:
            for i in range(len(self.values)):
                ret.append([other * self.values[i][0]])
        return ret

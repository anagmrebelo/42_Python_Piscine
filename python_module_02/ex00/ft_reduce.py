# import functools
# import operator

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively. Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator). Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function. 
    """
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Second argument is not iterable")
    if not callable(function_to_apply):
        raise TypeError("Second argument is not callable")
    
    ret = iterable[0]
    try:
        for i in iterable[1:]:
            ret = function_to_apply(ret, i)
        return ret
    except Exception:
        return None

# def main():
#     lst = ['H', 'e', 'l', 'l', 'o']
#     print(ft_reduce(lambda u, v: u + v, lst))
#     lis = [1, 3, 5, 6, 2]
#     print(functools.reduce(operator.add, lis))

# if __name__ == "__main__":
#     main()
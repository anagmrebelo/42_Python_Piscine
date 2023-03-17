def ft_filter(function_to_apply, iterable):
    """
        Filter the result of function apply to all elements of the iterable.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Return:
            An iterable.
            None if the iterable can not be used by the function.
    """
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Second argument is not iterable")
    if not callable(function_to_apply):
        raise TypeError("Second argument is not callable")
    try:
        for i in iterable:
            if function_to_apply(i) is True:
                yield i
    except Exception:
        return None

# def main():
#     x = [1, 2, 3, 4, 5]
#     ft_filter(lambda dum: not (dum % 2), x)
#     print(list(ft_filter(lambda dum: not (dum % 2), x)))

# if __name__ == "__main__":
#     main()
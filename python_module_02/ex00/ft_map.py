def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
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
    ret = []
    try:
        for i in iterable:
            yield function_to_apply(i)
    except Exception:
        return None

# def main():
#     x = [1, 2, 3, 4, 5]
#     ft_map(lambda dum: dum + 1, x)
#     print(list(ft_map(lambda t: t + 1, x)))

# if __name__ == "__main__":
#     main()
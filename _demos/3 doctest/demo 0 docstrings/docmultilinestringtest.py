def string_reverse(str1):
    """ Returns the reversed String.

    Parameters:
        str1 (str):The string which is to be reversed.

    Returns:
        reverse(str1):The string which gets reversed.   

    >>> string_reverse("jhohn")
    'nhohj'

    """
    reverse_str1 = ''
    i = len(str1)
    while i > 0:
        reverse_str1 += str1[ i - 1 ]
        i = i- 1
    return reverse_str1

# print(string_reverse('john'))

# print(string_reverse.__doc__)


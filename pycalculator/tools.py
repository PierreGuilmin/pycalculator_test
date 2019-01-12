"""This module implements various tool functions.

.. testsetup::

    from pycalculator.tools import *
"""

def color(string):
    r"""Add colors to string output in terminal.

    Parse the given string to replace every ``<symbol>`` block by its corresponding ANSI escape code, following this
    conversion table:
    
    +--------+------------------+---------+
    | symbol | ANSI escape code | meaning |
    +========+==================+=========+
    | ``</>``| ``'\x1b[0m'``    | reset   |
    +--------+------------------+---------+
    | ``<+>``| ``'\x1b[1m'``    | bold    |
    +--------+------------------+---------+
    | ``<r>``| ``'\x1b[31m'``   | red     |
    +--------+------------------+---------+
    | ``<g>``| ``'\x1b[32m'``   | green   |
    +--------+------------------+---------+
    | ``<b>``| ``'\x1b[34m'``   | blue    |
    +--------+------------------+---------+
    
    Warnings
    --------
    This method will not work on Windows terminal.

    Note
    ----
    This method automatically adds ``'\x1b[0m'`` (a reset escape sequence) to the end of the returned string to preserve
     the terminal output state.

    Parameters
    ----------
    string : `str`
        String to parse and print.

    Returns
    -------
    `str`
        ANSI encoded string.

    Examples
    --------
    .. doctest::

        >>> color('<r>ERROR: critical error.')
        '\x1b[31mERROR: critical error.\x1b[0m'

        >>> print(color('<g><+>All checks passed!')) # doctest: +SKIP
        All checks passed! # in green and bold in the terminal

    See Also
    --------
    `Wikipedia 'ANSI escape code' article <https://en.wikipedia.org/wiki/ANSI_escape_code>`_
    """

    ANSI_escape_code = {'</>': '\x1b[0m',  # reset
                        '<+>': '\x1b[1m',  # bold
                        '<r>': '\x1b[31m', # red
                        '<g>': '\x1b[32m', # green
                        '<b>': '\x1b[34m'} # blue

    for k, v in ANSI_escape_code.items():
        string = string.replace(k, v)

    # make sure to reset terminal state after the string has been printed
    string += '\x1b[0m'

    return string


if __name__ == '__main__':
    print('- normal')
    print(color('- <+>bold'))
    print(color('- <r>red'))
    print(color('- <g>green'))
    print(color('- <b>blue'))

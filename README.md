This module has been created to ease outputting data in terminal in table-like
form. To output data like that you need to pass the `data` list containing data
you want to print, and optional `header` (containing header row content) to
create a printable data structure like that

    >>> import pretty_printing as pp
    >>> header = ['Game', 'Rating']
    >>> data = [
    	['Super Mario Bros.', 'Very High'],
    	['GTA2', 'High'],
    	['Call of Duty: Modern Warfare', 'OMG! Ponies!']
    ]
    >>> print pp.PrettyTable(data, header=header)
    +------------------------------+--------------+
    | Game                         | Rating       |
    +------------------------------+--------------+
    | Super Mario Bros.            | Very High    |
    +------------------------------+--------------+
    | GTA2                         | High         |
    +------------------------------+--------------+
    | Call of Duty: Modern Warfare | OMG! Ponies! |
    +------------------------------+--------------+

Future releases will probably enable modification of such data and headers, plus
the ability to outline the header to be more visible.

Feel free to fork this, as well as add the issues and feature requests.

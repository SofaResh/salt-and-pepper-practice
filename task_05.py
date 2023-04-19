from datetime import datetime, timedelta


def date_in_future(integer=None):
    """
        >>> date_in_future([])==datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        True
        >>> date_in_future(2)==(datetime.now() + timedelta(days=2)).strftime("%d-%m-%Y %H:%M:%S")
        True
    """
    if integer is None or type(integer) != int:
        return (datetime.now()).strftime("%d-%m-%Y %H:%M:%S")
    return (datetime.now() + timedelta(days=integer)).strftime("%d-%m-%Y %H:%M:%S")

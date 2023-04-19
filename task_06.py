step = ["R", "P", "S"]


def rps_game_winner(arr):
    """
        >>> rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
        Traceback (most recent call last):
        ...
        Exception: WrongNumberOfPlayersError
        >>> rps_game_winner([['player1', 'P'], ['player2', 'A']])
        Traceback (most recent call last):
        ...
        Exception: NoSuchStrategyError
        >>> rps_game_winner([['player1', 'P'], ['player2', 'S']])
        'player2 S'
        >>> rps_game_winner([['player1', 'P'], ['player2', 'P']])
        'player1 P'
    """
    if len(arr) != 2:
        raise Exception("WrongNumberOfPlayersError")
    elif arr[0][1] not in step or arr[1][1] not in step:
        raise Exception("NoSuchStrategyError")
    elif arr[0][1] == arr[1][1]:
        return ' '.join(arr[0])
    else:
        if arr[0][1] == "R" and arr[1][1] == "S":
            return ' '.join(arr[0])
        elif arr[0][1] == "S" and arr[1][1] == "P":
            return ' '.join(arr[0])
        elif arr[0][1] == "P" and arr[1][1] == "R":
            return ' '.join(arr[0])
        else:
            return ' '.join(arr[1])

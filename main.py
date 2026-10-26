# working with dictionaries
from pyscript import display, document


def game_details(e):
    favorite_game = document.getElementById('dictionary').value.lower().strip()

    game_developers = {
        'roblox': 'David Baszucki',
        'codm': 'TiMi Studio',
        'fnaf': 'Scott Cawthon',
    }

    game_developers['genshin impact'] = 'HoYoverse'

    if favorite_game in game_developers:
        display(
            f"Game: {favorite_game.title()}",
            target='result',
            append=False
        )
        display(
            f"Developer: {game_developers[favorite_game]}",
            target='result'
        )
    else:
        display(
            "Game not found. Try Roblox, CODM, FNAF, or Genshin Impact.",
            target='result',
            append=False
        )

    list_with_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
    tuple_with_strings = (('ab', 'cd'), ('ef', 'gh'))
    list_with_strings = [('ax', 'one'), ('by', 'two'), ('cz', 'three')]

    display(dict(list_with_tuples), target='result')
    display(dict(tuple_with_strings), target='result')
    display(dict(list_with_strings), target='result')

    keywords = ['say', 'jm', 'jay', 'mace']
    value = ['esguerra', 'piansay', 'estrada', 'panela']

    students_nicknames = dict(zip(keywords, value))
    display(students_nicknames, target='result')

    philadelphia = {
        'center': 'joel embiid',
        'pf': 'lebron james',
        'sf': 'jaylen bronw',
        'sg': 'VJ edgecomb',
        'pg': 'tyrese maxey',
    }

    philadelphia['ph'] = 'stephen curry'
    del philadelphia['sg']
    display(philadelphia, target='result')

    dict1 = {'x': 1, 'y': 2, 'z': 3}
    dict2 = {'a': 4, 'b': 5, 'c': 6}

    display(dict1 | dict2, target='result')

    merged_dictionary = {**dict1, **dict2}
    display(merged_dictionary, target='result')

    display(len(merged_dictionary), target='result')

    ai = {
        'tony stark': 'creator',
        'Jarvis': 'AI1',
        'FRIDAY': 'AI2',
        'Edith': 'AI3',
        'Vision': 'AI4'
    }

    display('Vision' in ai, target='result')
    display(ai.get('Jarvis'), target='result')
    display(ai.keys(), target='result')
    display(ai.values(), target='result')
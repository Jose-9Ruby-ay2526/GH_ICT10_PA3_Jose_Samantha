
from pyscript import document

# Dictionary of game developers
game_developers = {
    'roblox': 'David Baszucki',
    'codm': 'TiMi Studio',
    'fnaf': 'Scott Cawthon',
    'genshin impact': 'HoYoverse'
}


def game_details(e=None):
    favorite_game = document.getElementById('dictionary').value.lower().strip()
    output = document.getElementById('result')

    if favorite_game in game_developers:
        developer = game_developers[favorite_game]

        output.innerHTML = f"""
            <strong>Game:</strong> {favorite_game.title()}<br>
            <strong>Developer:</strong> {developer}
        """

    else:
        output.innerHTML = """
            <span style="color: #d96f92;">
                Game not found. Try Roblox, CODM, FNAF, or Genshin Impact.
            </span>
        """

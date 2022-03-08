"""
    Beer song exercise
"""

def get_count(value):
    """
        Count bottle of beer
    """
    beer = str(value) if value != 0 else "No more"
    return beer + " bottles of beer" if value != 1 else beer + " bottle of beer"

def recite(start, take=1):
    """
        Recire the lyrics
    """
    result, beers = [], start
    for i in range(take):
        full = get_count(beers)
        result.append(full + " on the wall, " + full.lower() + ".")
        beers -= 1
        if beers >= 1:
            result.append("Take one down and pass it around, " + get_count(beers) + " on the wall.")
        elif beers == 0:
            result.append("Take it down and pass it around, no more bottles of beer on the wall.")
        else:
            beers = 99
            result.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
            break
        if i != take - 1:
            result.append("")
    for item in result:
        print(item)
    return result

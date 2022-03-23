"""
    ETL Excercise
"""
def transform(legacy_data):
    """
        Transform dict
    """
    result = {}
    for key, value in legacy_data.items():
        for char in value:
            result[char.lower()] = key
    return result

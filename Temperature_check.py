TEMP_MIN = 0
TEMP_MAX = 45

def temp_limit(temp):
    if temp < TEMP_MIN or temp > TEMP_MIN:
        print('Temperature is out of range!')
        return False
    return True

soc_min = 20
soc_max = 80

def soc_limit(soc):
    if soc < soc_min or soc > soc_max:
        print('State of Charge is out of range!')
        return False
    return True

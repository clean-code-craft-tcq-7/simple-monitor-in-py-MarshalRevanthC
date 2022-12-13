charge_rate_max = 0.8
charge_rate_min = 0.2

def charge_rate_limit(charge):
   if charge < charge_rate_min or charge > charge_rate_max:
        print('Charge rate is out of range!')
        return False
   return True

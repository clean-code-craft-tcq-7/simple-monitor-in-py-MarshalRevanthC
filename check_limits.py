import charge_rate
import soc_check
import Temperature_check

def battery_is_ok(temp,soc,charge):
  Temp_limits = Temperature_check.temp_limit(temp)
  soc_limits = soc_check.soc_limit(soc)
  charge_limits = charge_rate.charge_rate_limit(charge)

  if Temp_limits and soc_limits and charge_limits:
    return True
  return False


if __name__ == '__main__':
    assert (battery_is_ok(25, 70, 0.7) is True)
    assert (battery_is_ok(50, 85, 0) is False)

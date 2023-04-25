"""
Script adapted from https://github.com/custom-components/pyscript/wiki/Thermostat-Adjustment-using-Time-Trigger
"""

# A low temperatur to use as target temperature when I am not at home.
# It is better than turning it completely off, since I don't want the pipes to
# freeze. Later I should allow to set this value using the UI or a yaml file.
low_temp = 10 
normal_temp = 22

high_price = 1
high_price_temp = 18

def temperature_when_at_home():
    if sensor.nordpool > high_price:
        target_temp = high_price_temp
    else:
        target_temp = normal_temp
    climate.set_temperature(entity_id="climate.golvtermostat",
                            temperature=high_price_temp)



@time_trigger("once(7:30:00)")
def workday_energy_saving():
    """Trigger at 7:30am every"""
    
    # If it is a workday we set a low temperature
    if binary_sensor.workday == 'on':
        climate.set_temperature(entity_id="climate.golvtermostat",
                                temperature=low_temp)

@time_trigger("once(14:00:00)")
def work_day_heating():
    
    if binary_sensor.workday == 'on':
        temperature_when_at_home()

@time_trigger("once(8:30:00)")
def thermostat_nonwork_day():
    """Trigger at 8:30am every"""
    if binary_sensor.workday == 'off':
        temperature_when_at_home()

"""
Thermostat night script
"""
@time_trigger("once(23:00:00)")
def thermostat_night():
    """Trigger at 11pm every night"""
    climate.set_temperature(entity_id="climate.golvtermostat",
                            temperature=low_temp)

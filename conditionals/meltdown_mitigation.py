# 1. balanced criticality

def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    
    else:
        return False
print(is_criticality_balanced(750, 600))

    
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = current * voltage 
    efficiency = (generated_power/theoretical_max_power)*100

    if efficiency >= 80:
        band = "green"
    elif efficiency >= 60:
        band = "orange"
    elif efficiency >= 30:
        band = "red"
    else:
        band = "black"
    return band
print(reactor_efficiency(200,50,15000))



# Fail-safe mechanism to avoid overload and meltdown.
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    power = temperature * neutrons_produced_per_second
    if power < 0.9 * threshold:   #less than 90% of threshold
        return "LOW"
    
    if power <= 1.1 * threshold:
        "NORMAL"      # power btw 90% - 110%
    return "DANGER"
print(fail_safe(10, 44, 400))  #power > 110%

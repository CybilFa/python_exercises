EXPECTED_BAKE_TIME = 40
def bake_time_remaining(actual_minutes):
    return EXPECTED_BAKE_TIME - actual_minutes

def preparation_time_in_minutes(num_of_layers):
    return num_of_layers * 2      

def elapsed_time_in_mins(num_of_layers, elapsed_bake_time):
      """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
      return preparation_time_in_minutes(num_of_layers) + elapsed_bake_time

print('Expected bake time in mins: ', EXPECTED_BAKE_TIME)
print('-----------------------------------------------')
print('Bake time remaining:', bake_time_remaining(30))
print('-----------------------------------------------')
print('Preparation time: ', preparation_time_in_minutes(2))
print('-----------------------------------------------')
print('Elapsed time in mins:', elapsed_time_in_mins(3, 10)) #3*2 = 6, 6+10 = 16S


# output
# Expected bake time in mins:  40
# -----------------------------------------------
# Bake time remaining: 10
# -----------------------------------------------
# Preparation time:  4
# -----------------------------------------------
# Elapsed time in mins: 16

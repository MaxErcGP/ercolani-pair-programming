# Takes an input array and returns values scaled to lie in the range of 0.0 to 1.0.
def scale(arr):
    # import numpy for array operations
    import numpy as np
    
    # find the greatest value of the array, this will become the upper bound of ten
    arr_max = np.max(arr)
    
    # divide each value in the array by the max value, the max value will become 1
    # we must multiply by 10 then for the max to be 10, and then every value will be between 0 and 10
    arr_scaled = arr / arr_max * 10
    
    # returns the scaled array
    return arr_scaled
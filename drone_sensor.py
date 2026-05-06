def calculate_distance(velocity, time):
    # LOGIC ERROR: Distance should be velocity * time, not divided
    return velocity / time 


# TEST: If velocity is 50m/s and time is 2s, distance should be 100m.
# Currently this will return 25 (WRONG).
print(calculate_distance(50, 2))

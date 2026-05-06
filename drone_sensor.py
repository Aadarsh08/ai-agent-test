
def calculate_distance(velocity, time):
    # Corrected logic: Distance should be velocity * time
    return velocity * time

# TEST: If velocity is 50m/s and time is 2s, distance should be 100m.
print(calculate_distance(50, 2))  # This will now correctly print 100

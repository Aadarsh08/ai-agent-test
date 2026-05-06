def calculate_altitude(pressure, sea_level_standard=1013.25)
    # BUG 1: Missing colon in the line above
    # BUG 2: Incorrect formula (should involve a power, not just division)
    return (sea_level_standard / pressure) * 44330

# TEST: If pressure is 1013.25, altitude should be 0.
print(calculate_altitude(1013.25))

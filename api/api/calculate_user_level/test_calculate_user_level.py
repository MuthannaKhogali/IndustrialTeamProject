from calculate_user_level import calculate_user_level

def test_calculate_user_level():
    # Test cases for various user experience values, including edge cases. Change 2nd number to change expected levelf for assertion test.
    test_cases = [
        (0, 0),        # Minimum experience, should be level 0
        (50, 0),       # Low experience, should be level 0
        (483, 1),      # Exact Experience to hit level 1
        (1366, 2),     # Experience to achieve level 2
        (1400, 2),     # Experience should still be level 2
        (7198, 6),     # Experience for higher levels
        (12000, 8),     # Near the top level
        (2500000, 10),   # Very high experience, should max out at level 10
    ]
    
    # x and y values for testing, change to whatever you want!
    x = 0.35
    y = 1.5

    # ^ For x=0.35, y=1.5: ^
    # Level 1: 483 XP
    # Level 2: 1366 XP
    # Level 3: 2509 XP
    # Level 4: 3864 XP
    # Level 5: 5399 XP
    # Level 6: 7098 XP
    # Level 7: 8944 XP
    # Level 8: 10928 XP
    # Level 9: 13040 XP
    # Level 10: 15272 XP
    
    for user_experience, expected_level in test_cases:
        calculated_level = calculate_user_level(user_experience, x=x, y=y)
        assert calculated_level == expected_level, f"Test failed for XP {user_experience}. Expected {expected_level}, got {calculated_level}"
        print (calculated_level)
    
    print("All tests passed")

# Testing function for calculating level boundaries! Should help out if someone wants to tweak the x/y values!
def calculate_level_boundaries(x, y, max_level=10):
    boundaries = []
    
    for level in range(1, max_level + 1):
        # Calculate level boundary, multiply by 100, and round
        level_boundary = round((level / x) ** y * 100)
        boundaries.append(level_boundary)
    
    return boundaries

# Tests level boundaries! x value recommended between 0.3 and 0.4, y value between 1 and 2.
boundaries = calculate_level_boundaries(0.35, 1.5)
print("Level Boundaries:", boundaries)

# Run the test function
test_calculate_user_level()
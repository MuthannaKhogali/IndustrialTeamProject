import math

# Calculates user level based on current XP. Max level of 10.
# user_experience is the user's current XP, x & y represent difficulty.
# Level boundaries are calculated with (level / x)^y, rounded to nearest whole number, then multiplied by 100 to reflect our XP score.
# Returns user's level.
def calculate_user_level(user_experience, x=0.35, y=1.5):
    max_level = 10
    for level in range(1, max_level + 1):
        level_boundary = round((level / x) ** y * 100)
        if user_experience < level_boundary:
            return level - 1 if level > 0 else 0  # Return level 0 if no boundaries have been hit yet.
    return max_level  # Return level 10 if XP exceeds all boundaries
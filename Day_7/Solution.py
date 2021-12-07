from Input import crab_positions
from collections import Counter

crab_positions = Counter(crab_positions)

# starts point 0
fuel_to_reach_last_point = sum(
    k * v for k, v in crab_positions.items()
)
crabs_to_the_left = 0
crabs_to_the_right = sum(crab_positions.values()) - crab_positions.get(0, 0)
for i in range(1, max(crab_positions.keys())):
    crabs_to_the_left += crab_positions.get(i - 1, 0)
    fuel_to_reach_point_i = (
        fuel_to_reach_last_point + crabs_to_the_left - crabs_to_the_right
    )
    crabs_to_the_right -= crab_positions.get(i, 0)
    if fuel_to_reach_point_i > fuel_to_reach_last_point:
        print(fuel_to_reach_last_point)
        break
    fuel_to_reach_last_point = fuel_to_reach_point_i

# starts point 0
fuel_to_reach_last_point = sum(
    [(k * (k + 1) // 2) * v for k, v in crab_positions.items()]
)
for i in range(1, max(crab_positions.keys())):
    fuel_to_reach_point_i = fuel_to_reach_last_point
    for k, v in crab_positions.items():
        if k < i:
            fuel_to_reach_point_i += (i - k) * v
        if k >= i:
            fuel_to_reach_point_i -= (k - i + 1) * v
    if fuel_to_reach_point_i > fuel_to_reach_last_point:
        print(fuel_to_reach_last_point)
        break
    fuel_to_reach_last_point = fuel_to_reach_point_i

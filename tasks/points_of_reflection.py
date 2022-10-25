'''
    Task:
        Points of Reflection
'''

# Variables
points_1 = [0, 0], [1, 1]            # [2, 2]
points_2 = [2, 6], [-2, -6]          # [-6, 18]
points_3 = [10, -10], [-10, 10]      # [-30, 30]
points_4 = [1, -35], [-12, 1]        # [-25, 37]
points_5 = [1000, 15], [-7, -214]    # [-1014, -433]
points_6 = [0, 0], [0, 0]            # [0, 0]

# First solution
def symmetric_points(points):
    p, q = points

    return [q[0] - p[0] + q[0], q[1] - p[1] + q[1]]

# Second solution
def symmetric_points_2(points):
    p, q = points

    return [2 * q[0] - p[0], 2 * q[1] - p[1]]

# Output
print(symmetric_points(points_1))
print(symmetric_points(points_2))
print(symmetric_points(points_3))
print(symmetric_points(points_4))
print(symmetric_points(points_5))
print(symmetric_points(points_6))

print(symmetric_points_2(points_1))
print(symmetric_points_2(points_2))
print(symmetric_points_2(points_3))
print(symmetric_points_2(points_4))
print(symmetric_points_2(points_5))
print(symmetric_points_2(points_6))
'''
    Task:
        Points of Reflection
'''

# Variables
points1 = [0, 0], [1, 1]            # [2, 2]
points2 = [2, 6], [-2, -6]          # [-6, 18]
points3 = [10, -10], [-10, 10]      # [-30, 30]
points4 = [1, -35], [-12, 1]        # [-25, 37]
points5 = [1000, 15], [-7, -214]    # [-1014, -433]
points6 = [0, 0], [0, 0]            # [0, 0]

# First solution
def symmetric_points(points):
    p, q = points

    return [q[0] - p[0] + q[0], q[1] - p[1] + q[1]]

# Second solution
def symmetric_points_2(points):
    p, q = points

    return [2 * q[0] - p[0], 2 * q[1] - p[1]]

# Output
print(symmetric_points(points1))
print(symmetric_points(points2))
print(symmetric_points(points3))
print(symmetric_points(points4))
print(symmetric_points(points5))
print(symmetric_points(points6))

print(symmetric_points_2(points1))
print(symmetric_points_2(points2))
print(symmetric_points_2(points3))
print(symmetric_points_2(points4))
print(symmetric_points_2(points5))
print(symmetric_points_2(points6))
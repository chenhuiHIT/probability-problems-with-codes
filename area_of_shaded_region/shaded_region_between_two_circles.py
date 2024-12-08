"""
let the left down point be (0,0) and right top point be (1,1)
"""
import numpy as np

def run(repeat_nums):
    random_points = np.random.uniform(0, 1, (repeat_nums, 2))
    left_circle_center = np.array([0, 0.5])
    right_circle_center = np.array([1, 0])
    distance_2_left = np.linalg.norm(random_points - left_circle_center, axis=1)
    distance_2_right = np.linalg.norm(random_points - right_circle_center, axis=1)
    area = sum(np.logical_and((distance_2_left <= 0.5), (distance_2_right <= 1))) / repeat_nums
    return area

if __name__=="__main__":
    nums = 100000000
    result = run(nums)
    print("the area of shaded region is {}".format(result*400))
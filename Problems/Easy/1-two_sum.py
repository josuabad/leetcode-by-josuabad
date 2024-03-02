class Solution:
    @staticmethod # For ease on testing, we declare a staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        Restrictions:
            · Assuming that each input would have exactly one solution
            · Without using the same element twice

        Args:
            nums (list[int]): List of integers.
            target (int): Target sum.

        Returns:
            list[int]: Indices of the two numbers that add up to target.
        """
        for num_x in range(len(nums)): # Iterate through each element in the list
            for num_y in range(num_x + 1, len(nums)): # Repeats iteration avoiding using the same element twice
                if nums[num_x] + nums[num_y] == target: # Check sum result
                    return [num_x, num_y]  # If found, return the indices of the two numbers
        return []  # If no solution is found, return an empty list


if __name__ == "__main__":
    pass

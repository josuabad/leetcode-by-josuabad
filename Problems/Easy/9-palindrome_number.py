class Solution:
    @staticmethod # For ease on testing, we declare a staticmethod
    def isPalindrome(x: int) -> bool:
        """
        Given an integer x, return true if x is a palindrome, and false otherwise.

        Args:
            x (int): Input integer.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """
        x = str(x) # Convert the integer to a string
        x_num_values = len(x) # Get the number of characters in the string
        for pointer_left in range(x_num_values): # Iterate through each character in the string
            pointer_right = x_num_values - pointer_left - 1
            if x[pointer_left] != x[pointer_right]: # Check if the character at the current position matches the character at the symmetric position
                return False  # If not, return False (not a palindrome)
            if pointer_left >= pointer_right: # Check if the pointer reaches the middle of the string
                return True  # If so, return True (is a palindrome)


if __name__ == "__main__":
    pass

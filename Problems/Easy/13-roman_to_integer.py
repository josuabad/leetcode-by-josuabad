class Solution:
    @staticmethod # For ease on testing, we declare a staticmethod
    def romanToInt(roman_number: str) -> int:
        """
        Given a roman numeral, convert it to an integer.

        Args:
            s (str): roman number

        Returns:
            int: integer number
        """
        sum = 0  # Sum of all input roman letters
        roman_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}  # Equity between letters and numbers
        check_num = True # Check if the following number needs to be done

        for index in range(len(roman_number)):
            if check_num == False:
                check_num = True
                continue
            letter = roman_number[index].upper()
            try:  # There might not be another step because it's the end of the string
                next_letter = roman_number[index + 1].upper() # We always verify the next one in case there's any applied rule
                if letter == "I":
                    if next_letter == "V":
                        sum += 4
                        check_num = False
                    elif next_letter == "X":
                        sum += 9
                        check_num = False
                    else:
                        sum += 1
                elif letter == "X":
                    if next_letter == "L":
                        sum += 40
                        check_num = False
                    elif next_letter == "C":
                        sum += 90
                        check_num = False
                    else:
                        sum += 10
                elif letter == "C":
                    if next_letter == "D":
                        sum += 400
                        check_num = False
                    elif next_letter == "M":
                        sum += 900
                        check_num = False
                    else:
                        sum += 100
                else:
                    sum += roman_nums.get(letter)
            except IndexError: # End of the String
                sum += roman_nums.get(letter)
        return sum


if __name__ == "__main__":
    pass

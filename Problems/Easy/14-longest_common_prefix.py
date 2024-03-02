class Solution:
    @staticmethod # For ease on testing, we declare a staticmethod
    def longestCommonPrefix(strs: list[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        Args:
            strs (list[str])

        Returns:
            str: prefixes or "" if no prefix found
        """
        try:
            base = strs[0].lower() # Verifica la palabra entera
        except:
            return ""
        for word in strs[1:]: # Descarta la primera palabra
            for letter in range(len(base)): # Comprobación
                try:
                    if base[letter] != word[letter]:
                        base = base[:letter]
                        break
                except IndexError: # Cuando la palabra base > palabra comprobada
                    base = base[:len(word)]
        if len(base) == 0:
            return ""
        return base


if __name__ == "__main__":
    pass

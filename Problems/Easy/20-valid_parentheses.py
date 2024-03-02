class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        if len(s) < 2:
            return False # Imposible buena sintaxis
        stack = [] # list as stack
        for ltr in s:
            if ltr in "([{":
                stack.append(ltr)
            elif ltr in ")]}":
                if stack == []:
                    return False
                previous_parentheses = stack.pop()
                if ltr == ")" and previous_parentheses == "(":
                    continue
                elif ltr == "]" and previous_parentheses == "[":
                    continue
                elif ltr == "}" and previous_parentheses == "{":
                    continue
                else:
                    return False
        return stack == [] # No hay más comparaciones pendientes


if __name__ == "__main__":
    pass

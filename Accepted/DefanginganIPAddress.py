class Solution:
    def defangIPaddr(self, address: str) -> str:
        charList = []
        for item in address:
            if item == ".":
                charList.append("[")
                charList.append(".")
                charList.append("]")
            else:
                charList.append(item)
        output = "".join(charList)
        return output

    
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ""
        for x in digits:
            result += str(x)
        x = int(result)+1
        y = str(x)
        final = []
        for val in y:
            final.append(int(val))
        return final
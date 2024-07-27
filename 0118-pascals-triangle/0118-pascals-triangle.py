class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        List = [[1]]
        for i in range(numRows-1):
            temp = [0]+List[-1]+[0]
            new = []
            for j in range(len(List[-1])+1):
                new.append(temp[j]+temp[j+1])
            List.append(new)
        return List
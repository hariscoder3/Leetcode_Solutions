class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        left = 0
        right = len(people)-1
        total = 0
        while left<=right:
            total = people[left]+people[right]
            if total<=limit:
                print(total)
                boat+=1
                left+=1
                right-=1
                print("<=")
            else:
                print("else")
                if people[right]<=limit:
                    boat+=1
                    right-=1
                    print("r")
                elif people[left]<=limit:
                    boat+=1
                    left+=1
                    print("l")
        # print(left)
        # print(right)
        return boat
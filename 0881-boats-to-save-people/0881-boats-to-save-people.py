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
                boat+=1
                left+=1
                right-=1
            else:
                if people[right]<=limit:
                    boat+=1
                    right-=1
                elif people[left]<=limit:
                    boat+=1
                    left+=1
        return boat
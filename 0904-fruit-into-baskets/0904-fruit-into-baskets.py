class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        start = 0
        for f in fruits:
            basket[f] += 1
            if len(basket) > 2:
                basket[fruits[start]] -=1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start+=1
        return len(fruits)-start;
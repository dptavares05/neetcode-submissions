class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {} ## create a hashMap with the key being the number and value the frequency of the number

        for i in nums:
            ##count how many times each number(key) appears(value)
            hashMap[i] = 1 + hashMap.get(i, 0)

        #sort each number by frequency and then reverse it
        sortedKeys = sorted(hashMap.keys(), key=hashMap.get, reverse=True)

        # return only the first k numbers
        return sortedKeys[:k]



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            
            countS, countT = {}, {}

            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            
            for j in countS:
                if countS[j] != countT.get(j, 0):
                    return False
            return True

        outputList = []

        for word in strs:
            matched = False

            for group in outputList:
                if isAnagram(word, group[0]):
                    group.append(word)
                    matched = True
                    break
            if not matched:
                outputList.append([word])
        return outputList

            


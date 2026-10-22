class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        targetCount = [0]*26
        for letter in s1:
            targetCount[ord(letter) - ord('a')] += 1


        seenCount = [0] * 26
        left = 0
        for right in range(len(s2)):
            seenCount[ord(s2[right]) - ord('a')] += 1
            if targetCount == seenCount: return True

            while (right-left+1) >= len(s1):
                seenCount[ord(s2[left]) - ord('a')] -= 1
                left += 1

        return False

            
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count = Counter(s1)
        s2count = Counter(s2[:len(s1)])
        print(s1count, s2count)
        j=0
        for i in range(len(s1), len(s2)):
            if s1count == s2count: return True

            s2count[s2[i]] += 1
            s2count[s2[j]] -= 1

            if s2count[s2[j]] == 0:
                del s2count[s2[j]]
            j += 1
            print(s1count, s2count)
        return s1count == s2count

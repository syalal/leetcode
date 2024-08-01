class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)

        num1 = num1[::-1]
        num2 = num2[::-1]

        res = [0]*(l1+l2)

        for i in range(l1):
            for j in range(l2):
                mul = int(num1[i])*int(num2[j])
                res[i+j] += mul
                res[i+j+1] += res[i+j]//10
                res[i+j] = res[i+j]%10

        res_str = ''.join(map(str, res[::-1])).lstrip('0')

        return res_str if len(res_str) > 0 else '0'
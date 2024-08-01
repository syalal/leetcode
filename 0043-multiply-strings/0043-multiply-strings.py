class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num_mapping = {str(i):i for i in range(10)}

        def string_to_num(str_num):
            num = 0 
            for char in str_num:
                num = num*10 + num_mapping[char]
            return num

        num1 = string_to_num(num1)
        num2 = string_to_num(num2)

        return str(num1*num2)


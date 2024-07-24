class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        divisors = [e for e in range(0, n, k)]
        count_substring = {}
        for i in divisors:
            count_substring[word[i:i+k]] = count_substring.get(word[i:i+k], 0) + 1
        print(count_substring)

        max_substring = [k for k,v in count_substring.items() if v==max(count_substring.values())][0]
        rest_substring_count = sum([v for k,v in count_substring.items() if k!=max_substring])

        return rest_substring_count




# class Solution:
#     def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
#         n = len(word)
#         if k==1:
#             c = Counter(list(word))
#             update_count = sum(c.values()) - max(c.values()) 
#             return update_count

#         def update_substring(word, i, j, k):
#             print(word, i, j, k)
#             replace_substring = word[j:j+k] 
#             # word[i:i+k-1] = word[j:j+k-1] 
#             res = word[:i]+replace_substring+word[i+k:]
#             print(f"resplace: {replace_substring}")
#             print(f"updated string: {res}")
#             return res

#         divisors = [e for e in range(0, n, k)]

#         def check_periodic(word_, k):
#             count_substring = {}
#             for i in divisors:
#                 count_substring[word_[i:i+k]] = count_substring.get(word_[i:i+k], 0) + 1
#                 print(count_substring)

#             if len(divisors)==1:
#                 return True
#             else:
#                 return count_substring
        
#         def substring_index(word_main, sub_string, k):
#             for i in range(0, len(word_main), k):
#                 if sub_string == word_main[i:i+k]:
#                     return i
#                 else:
#                     continue


#         i = divisors[0]
#         j = divisors[1]
#         update_count = 0
#         updated_string = word
#         while update_count<=len(word):
#             updated_string = update_substring(updated_string, i, j, k)
#             update_count += 1
#             print(f"update count: {update_count}")
#             word_periodic = check_periodic(updated_string, k)
#             if word_periodic == True:
#                 return update_count
#             else:
#                 max_substring = [k for k,v in word_periodic.items() if v==max(word_periodic.values())][0]
#                 min_substring = [k for k,v in word_periodic.items() if v==min(word_periodic.values())][0]
                
#                 i = substring_index(updated_string, min_substring, k) 
#                 j = substring_index(updated_string, max_substring, k)             


        
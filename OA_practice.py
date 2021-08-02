def Solution(A):
    # n = len(A)
    # pairs = n // 2
    # left = n // 2 - 1
    # right = n // 2
    # total = sum(A)
    # target_sum =  total // pairs
    # res = float("inf")
    # A.sort()
    # while left >= 0 and right <= n - 1:
    #     temp_target = A[left] + A[right]
    #     temp_res = temp_target - target_sum
    #     left -= 1
    #     right += 1
    #     if temp_res > 0:
    #         res = min(res, temp_res)
    # return res + target_sum if res != float("inf") else target_sum
    res = 0
    n = len(A)
    for i in range(3, n + 1):
        res += Solution2(i, A)
    return res

# A = [4,5,3,1]
# B = [2,4,1,5,6,7]
# C = [1,2,3,100]
# D = [2,3,1,1]
# E = [-5,-6]
# F = [-3,-4,-5,-6]
# res1 = Solution(A)
# res2 = Solution(B)
# res3 = Solution(C)
# res4 = Solution(D)
# res5 = Solution(E)
# res6 = Solution(F)
# print(res1)
# print(res2)
# print(res3)
# print(res4)
# print(res5)
# print(res6)



def Solution2(a,A):
    if not A:
        return []
    n = len(A)
    res = []
    def dfs(temp_res,index,res):
        if len(temp_res) == a:
            res.append(temp_res)
        for i in range(index,n):
            dfs(temp_res + [A[i]], i + 1, res)
        
    dfs([],0,res)
    return len(res)

    
A = [4,6,5,10]
res = Solution(A)
print(res)
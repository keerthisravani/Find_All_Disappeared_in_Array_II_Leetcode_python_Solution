def findDuplicates(nums):
    n=len(nums)
    l=[0]*(n+1)
    for i in nums:
        l[i]+=1
    result=[]
    for i in range(1,n+1):
        if l[i]==2:
            result.append(i)
    return result
nums=[1,2,3,2,4,5,6,5]
print(findDuplicates(nums))


    
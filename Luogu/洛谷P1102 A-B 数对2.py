n,c=map(int,input().split())
nums=list=list(map(int,input().split()))
count_dict={}
pair_count=0
for num in nums:
    if num -c in count_dict:
        pair_count +=count_dict[num -c]
    count_dict[num] =count_dict.get(num,0) +1
print(pair_count)
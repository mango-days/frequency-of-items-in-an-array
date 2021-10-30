array=["a","b","a","b","c"]
dict={}
for x in array:
    if x in dict.keys(): dict[x]+=1
    else: dict[x]=1
print(dict)
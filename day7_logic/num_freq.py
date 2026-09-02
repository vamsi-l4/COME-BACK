num=list(map(int,input("emter the num: ").split()))
freq={}
for nums in num:
    if nums in freq:
        freq[nums]+=1
    else:
        freq[nums]=1
for ch in freq:
    print(ch,':',freq[ch])            
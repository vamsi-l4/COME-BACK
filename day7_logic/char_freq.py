text=input("enter the text: ")
freq={}
for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for ch in freq:        
    print(ch,":",freq[ch])            
n = int(input())
a = list(map(str,input().split()))
freq = {}

for ch in a:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
max_freq = max(freq.values())
for keys,values in freq.items():
    if values == max_freq:
        print(keys)
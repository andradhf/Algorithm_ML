def merge_srt(s):
    n = len(s)
    if n > 1:
        print(s)
        mid = n // 2
        l, r = s[:mid], s[mid:]
        merge_srt(l)
        merge_srt(r)
        merge(s,l,r)
        
def merge(s,l,r):
    k = 0 
    while len(l) > 0 and len(r) > 0 :
        if l[0] <= r[0]:
            s[k] = l.pop(0)
        else:
            s[k] = r.pop(0)
        k += 1
    
    while len(l) != 0:
        s[k] = l.pop(0)
        k += 1
    while len(r) != 0:
        s[k] = r.pop(0)
        k += 1
        
s = [27,10,12,20,25,13,15,22]
merge_srt(s)
print(s)
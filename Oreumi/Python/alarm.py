H, M = map(int, input().split())

if(M<45):
    if(H<1):
        H=23
    else:
        H-=1
    M=M+60-45
else:
    M-=45
print(str(H)+" "+str(M))
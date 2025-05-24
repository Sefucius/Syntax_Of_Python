s=[88,89,90,98,00,99]
print(s)
for i in range(len(s)):
    if s[i]==0:
        s[i]='200'+str(s[i])
    else:
        s[i]='19'+str(s[i])
print(s)

print('-'*20)

s=[88,89,90,98,00,99]
print(s)
for index,value in enumerate(s):
    if value==0:
        s[index]='200'+str(value)
    else:
        s[index]='19'+str(value)
print(s)
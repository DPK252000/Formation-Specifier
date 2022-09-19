p=6; y=9.9; d='pavan'
print(type(p),type(y),type(d))
print(p)
print('%d' %p)
print('%i' %p)
print('%f' %y)
print('%.1f' %y)
print('%.2f' %y)
print('%.6f' %y)

p=9
print(float(p))
print(str(p))
print('%f' %p)
print('%s' %p)

p=9.1
print(int(p))
print(float(p))

p='pavan'
print(type(p))
y=int(p)
print(y,type(y))
f=float(p)
print(f,type(f))

k='3.9'
print(type(k))
print(int(k)) #valueerror
a=float(k)
print(a,type(a))
i=int(a)
print(i,type(i))

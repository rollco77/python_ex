
# tuple은 수정이 불가한 집합
a = (3,)
b = (10,12,13)
c =  21, 22, 23

print(a[0])
print(b)
print(c[2])


#dictionary
dic = {'name':'수' , 'age':40}
print(dic)
print(dic.get('name'))

print(dic.keys)

dic['phoneno'] = '01011111111'

print(dic)
print(dic['phoneno'])
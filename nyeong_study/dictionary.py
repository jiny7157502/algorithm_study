# dictionary : key와 value로 이루어진 자료형
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}

a = {1 : 'a'}
a[2] = 'b'
a # {1 : 'a', 2 : 'b'}

a['name'] = 'pey'
a # {1 : 'a', 2 : 'b', 'name' : 'pey'}

a[3] = [1,2,3]
a # {1 : 'a', 2 : 'b', 'name' : 'pey', 3 : [1,2,3]}

del a[1]
a # {2 : 'b', 'name' : 'pey', 3 : [1, 2, 3]}

a[2] # 'b'
a.get('name') # 'pey'

b = {1 : 'a', 1 : 'b'}
b # {1 : 'b'}

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(list(a.keys())) # 키 얻기 ['name', 'phone', 'birth']
print(list(a.values())) # 값 얻기 ['pey', '0119993323', '1118']
print(list(a.items())) # 쌍 얻기 : [('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]
a.clear() # 딕셔너리 안의 모든 요소 삭제 : {}
'name' in a # in : 해당 키가 딕셔너리 안에 있는지 조사 = True
'email' in a # False

data={0:12,1:13,2:15,3:16,4:17}
print(data)

data={'manoj':11,'jagan':22,'vihan':33}
print(data)

keys={'manoj','jagan','vihan'}
values={11,22,33}
data=dict(zip(keys,values))
print(data)

data.get('jagan')
print(data.get('jagan'))

del data['manoj']
print(data)

data={'python':'pyspark','java':'spring','js':'css'}
print(data)

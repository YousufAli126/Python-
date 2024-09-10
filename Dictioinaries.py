#Dictionaries 
cc = {'Pakistan':'Karachi',
      'Russia':'Moscow',
      'Japan':'Tokyo',
      'USA':'Washington DC'}
#print(cc['Pakistan'])
#print(cc.get('Czech Republic'))
#print(cc.keys())
#print(cc.values())
#print(cc.items())
#cc.pop('USA')
#cc.clear()

#cc.update({'China':'Beijing'})

for key, value in cc.items():
    print(key, value)
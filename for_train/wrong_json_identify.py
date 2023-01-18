import json


texti=0
error_cnt=0
error_list=[]
for texti in range(1):
    try:
        f2 = open(".\\small_json\\small_json_"+str(texti)+".json", 'r',encoding='unicode_escape')
        j=json.load(f2)
        print(texti,"finload")
        print(j[0]['tokens'][0][0])
        f2.close()
    except Exception as e:
        print(e)
        print(texti,"error")
        error_cnt+=1
        error_list.append(texti)
print(error_cnt)
print(error_list)
# error file is 4,32 [4, 14, 102, 111, 114, 185, 189, 234, 251, 259, 279, 318, 321, 348, 353, 442, 445, 483]
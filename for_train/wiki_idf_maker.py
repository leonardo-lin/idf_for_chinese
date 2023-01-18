

import json
import math

texti=0
word_feq={}
error_list=[]
#samefile=[][4, 24, 114, 185, 189, 211, 251, 290, 321, 331, 353, 379, 435, 445, 451, 485]
for texti in range(486):
    
    try:
        f2 = open(".\\small_json\\small_json_"+str(texti)+".json", 'r',encoding='unicode_escape')
        jfile=json.load(f2)
        print(texti,"finload")
        print(jfile[0]['tokens'][0][0])
        #提取每篇文章
        for each_f in range(len(jfile)):
            #print("file = ",each_f)
            samefile=[]
            #提取每個句子
            for each_sen in jfile[each_f]['tokens']:
                #p=input()
                #print(each_sen) 
                    
                #提取每個字
                for each_word in each_sen:               
                    #print(each_word[0])
                    if each_word[0] not in word_feq:
                        word_feq[each_word[0]]=[1,1]
                        samefile.append(each_word[0])
                    else:
                        if each_word[0] not in samefile:
                            samefile.append(each_word[0])
                            #print(samefile)
                            word_feq[each_word[0]][0]+=1
                            word_feq[each_word[0]][1]+=1
                        else:
                            word_feq[each_word[0]][0]+=1
                #print(word_feq)
                #rint(samefile)    
                    
                    
        f2.close()
    except:
        print("error in =" ,texti)
        error_list.append(texti)
        pass
#print(word_feq)
#計算idf
for i in word_feq:
    #p=input()
    #print(word_feq[i],word_feq[i][0],word_feq[i][1])
    word_feq[i] = math.log(word_feq[i][0]/(word_feq[i][1]+1),2)
word_feq=sorted(word_feq.items(),key=lambda x:x[1],reverse = True)
word_feq=dict(word_feq)
f=open("idf.json","w",encoding="utf-8")
output2 = json.dumps(word_feq,ensure_ascii=False)     # 產生要寫入的資料
f.write(output2)        # 寫入資料
f.close()

print(error_list)
for i in word_feq:
    p=input()
    print(i,word_feq[i])
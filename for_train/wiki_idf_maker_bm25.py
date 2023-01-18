

from rank_bm25 import BM25Okapi
import json
corpus=[]
texti=0
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
            a_file=[]
            #提取每個句子
            for each_sen in jfile[each_f]['tokens']:
                #p=input()
                #print(each_sen) 
                    
                #提取每個字
                for each_word in each_sen:               
                    #print(each_word[0])
                    a_file.append(each_word[0])
                #print(word_feq)
                #rint(samefile)    
            corpus.append(a_file)        
                    
        f2.close()
    except:
        print("error in =" ,texti)
        error_list.append(texti)
        pass
print(len(corpus))
print(error_list)

bm25 = BM25Okapi(corpus) 
bm25=bm25.idf


print(type(bm25))
f=open("bm25_idf.json","w",encoding="utf-8")
output = json.dumps(bm25,ensure_ascii=False)     # 產生要寫入的資料
f.write(output) # 寫入資料
print('finwrite')
f.close()
for i in bm25:
    p=input()
    print(i)
    print(i,bm25[i])
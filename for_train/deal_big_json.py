
import json

f=open("wiki_tokenize_2021_08_05_1215639.txt",'r',encoding='unicode_escape')
texti=0
cnt=0
tx_i=f.read()

tx=''
dropcomma=0
start=False
end=False
for i in tx_i:
    
    """if start==True:
        if dropcomma<2:
            dropcomma+=1
        else:   """ 
    if texti==0:    
        tx=tx+i
    else:
        if dropcomma<2:
            dropcomma+=1
        else:
            tx=tx+i
    if i=='}':
        cnt=cnt+1
        """if cnt==(texti*1000)+1:
            start=True
            print("start",start,cnt)"""
        if cnt%500==0:
            print(cnt)
        if cnt==(texti+1)*2500:
            print("end",start,cnt)
            dropcomma=0
            
            tx=tx+"]"
            print("openfile",str(texti))
            f2 = open(".\\small_json\\small_json_"+str(texti)+".json", 'w',encoding='unicode_escape')
            f2.write(tx)
            f2.close()
            print("fine")
            
            #next file
            texti+=1
            tx='['
            dropcomma=0
    
        
    


f.close()


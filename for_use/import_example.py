
import load_idf
p='竹北市'
print(p,load_idf.load(p))
p='上午'
print(p,load_idf.load(p))


import bm25_load_idf
p='竹北市'
print(p,bm25_load_idf.load(p))
p='上午'
print(p,bm25_load_idf.load(p))

import json
def load(searcher):
    f2 = open("bm25_idf.json", 'r',encoding='utf-8')
    idf=json.load(f2)
    return idf[searcher]
    
    
if __name__ == '__main__':
    print('in')
    print(load('李青萍'))
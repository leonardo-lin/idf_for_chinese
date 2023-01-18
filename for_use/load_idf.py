
import json
def load(searcher):
    f2 = open("idf.json", 'r',encoding='utf-8')
    idf=json.load(f2)
    return idf[searcher]
    
    
if __name__ == '__main__':
    print(load('竹北市'))
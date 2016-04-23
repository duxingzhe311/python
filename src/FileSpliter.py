def getFileMap(filepath):
    key = ''
    val = []
    file = open(filepath,'r')
    res = {}
    
    while True:
        line = file.readline()
        
        if line and line.strip() == '':
            res[key] = val
            val = []
            key = ''
            continue
        
        if line:
            val.append(line)
            if key == '':
                key = line.strip()
                
        else:
            if key != '':
                res[key] = val
                val = []
                key = ''
            break
        
    file.close()
    
    return res


def makeFile(fileName,fileData):
    f = open(fileName,'a')
    for line in fileData:
        f.write(line)
    f.close()



basePath = 'C:\\Users\\Administrator\\Desktop\\pp\\'
 
print('start...')

res = getFileMap(basePath + 'pp.txt')
for key in res:
    fn = basePath + key + '.txt';
    print('create file ' + fn + ' start...')
    makeFile(fn,res[key])
    print('create file ' + fn + ' over...')

print('over...')

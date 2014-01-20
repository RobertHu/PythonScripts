import re , sys

def output(macName,namespaceName,lines,needNamespace,filePath):
    with open(filePath,mode='w',encoding='utf-8') as a_file:
        for line,needNewLine in getOutputContent(macName,namespaceName,lines,needNamespace):
            appendLine(a_file,line,needNewLine)

def getOutputContent(macName,namespaceName,lines,needNamespace):
    marcs = list(getMacros(macName))
    namespaces = list(getnamespaceTemplate(namespaceName)) if needNamespace else None
    yield (marcs[0],True)
    yield(marcs[1],True)
    if needNamespace: 
        yield(namespaces[0],True) 
        yield (namespaces[1],True)
    for line in lines:
        yield (line,False)
    if needNamespace:
        yield ("\n",False)
        yield (namespaces[2],True)
    yield (marcs[2],True)


        

def getnamespaceTemplate(name):
    yield 'namespace ' + name
    yield '{'
    yield '}'

def getMacros(input):
    yield r'#ifndef ' +'_' + input.upper() + '_H'
    yield r'#define ' + '_' + input.upper() + '_H'
    yield r'#endif'

def appendLine(file,content,addLine = False):
    if addLine:
        file.write(content + '\n')
    else:
        file.write(content)

def generateClassTemplate(classname):
    template='''
    class {}
    {{
    }};
    '''
    return template.format(classname)

if __name__ == '__main__':
    nsname = sys.argv[1]
    class_name = sys.argv[2]
    needNamespace = True if nsname else False
    content = generateClassTemplate(class_name)
    output(class_name,nsname,content,needNamespace,'source.txt')
    print('done')




    

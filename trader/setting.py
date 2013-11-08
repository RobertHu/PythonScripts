import re
file_name = r'D:\Teams\iExchangeCollection\iExchange3 Team\TradingConsole.Silverlight\Common\TradingSet.cs'

save_file_name = 'trading.txt'

settings = []

filter = 'public'

pattern = '(\w+).*'

remove_get_set_pattern = '\{.*\}$'


def fetchFileName(input):
    return re.sub(pattern,r'\1',input)
    


with open(file_name,encoding='utf-8',mode='r') as a_file:
    for a_line in a_file:
        if filter in a_line:
            if re.search(remove_get_set_pattern,a_line):
                a_line=re.sub(remove_get_set_pattern,'',a_line)
            p,type,name = a_line.split(None,3)
            target = fetchFileName(type)
            settings.append(target)
        

with open(save_file_name,encoding='utf-8',mode='w') as a_file:
    for fn in {f for f in settings}:
        a_file.write(fn + '\n')




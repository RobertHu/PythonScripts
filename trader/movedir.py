import os
import shutil  

cwd = r'D:\Teams\iExchangeCollection\iExchange3 Team\TradingConsole.Silverlight\Common'

dst_dir=r'D:\Work\Python\trader\trading'

file_name= 'trading.txt'

with open(file_name,mode='r',encoding='utf-8') as a_file:
    myjoin = lambda name, dir : os.path.join(dir,name)
    for f in a_file:
        src = f.strip() + '.cs'
        dst_file = myjoin(src,dst_dir)
        src_file = myjoin(src,cwd)
        try:
            shutil.copy(src_file,dst_file)
        except FileNotFoundError:
            print('copy error '+ f)



#files = []
#for (dirpath, dirnames, filesnames) in os.walk(cwd):
#    files.extend(filesnames)
#    break

#for f in files:
#    print(f)



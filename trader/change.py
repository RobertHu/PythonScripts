import os, stat

result = []
#cwd = r'D:\Teams\iExchangeCollection\iExchange3 Team\iExchange3Promotion\AsynchronousSslStream\CppTrader\DataMapping'
cwd = r'D:\Work\Python\trader\trading'
for root, dirs, files in os.walk(cwd):
    result.extend(files)
    break

result_files = [os.path.join(cwd,f) for f in result]

for item in result_files:
    os.chmod(item, stat.S_IWRITE)   
print('done')


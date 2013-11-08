import re
input_file_name = 'input.txt'
output_file_name = 'result.txt'
pattern = '.*=\s*"(.*)";$'
result = []

with open(input_file_name,mode='r',encoding='utf-8') as a_file:
    for line in a_file:
        match = re.search(pattern,line)
        if match:
            result.append(match.group(1))

with open(output_file_name,mode='w',encoding='utf-8') as a_file:
    for name in result:
        a_file.write(name + ',\n')


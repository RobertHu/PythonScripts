import json, os, glob,datetime,time,shutil

def getSpecificDirPartForLast(path,n):
    root, dir = os.path.split(path)
    if n == 0:
        return dir
    return getSpecificDirPartForLast(root, n - 1)

def getDirPartInPath(path,part_numbers):
    result= []
    for n in part_numbers:
        result.append(getSpecificDirPartForLast(path,n))
    return result

def getAllFilesInSpecificDay(files,date):
    for file in files:
        m_time = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        if m_time.year == date.year and m_time.month == date.month and m_time.day == date.day:
            yield file

def copyFileToSpeciftDest(files,host):
    for file_path in files:
        dir, name = os.path.split(file_path)
        dir_parts = getDirPartInPath(file_path,host['parts'])
        print(dir_parts)
        dest_dir =os.path.join(host['dest'],*dir_parts)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        dest_path = os.path.join(dest_dir,name)
        shutil.copyfile(file_path,dest_path)

def copy(host,file_types):
    today = datetime.datetime.today()
    target = []
    for file_type in file_types:
        files=glob.glob(os.path.join(host['source'],file_type))
        for file in getAllFilesInSpecificDay(files,today):
            target.append(file)
    copyFileToSpeciftDest(target,host)


if __name__ == '__main__':
    print('start')
    configs = None
    with open('config.json','r',encoding='utf-8') as f:
        configs = json.load(f)

    filetypes = ['*.dll', '*.exe']
    copy(configs['client'],filetypes)
    copy(configs['server'],filetypes)







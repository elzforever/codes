import os,sys

def rename_files(path,pos):
    for file in os.listdir(path):
        if file=='4.bmp':
            pos1 = pos*3-2
            new_name = '00000006_0' + str(pos1) + '.bmp'
            os.rename(os.path.join(path,file), os.path.join(path, new_name))
            print(new_name)
        elif file=='5.bmp':
            pos1 = pos*3-1
            new_name = '00000006_0' + str(pos1) + '.bmp'
            os.rename(os.path.join(path,file), os.path.join(path, new_name))
            print(new_name)
        elif file=='6.bmp':
            pos1 = pos*3
            new_name = '00000006_0' + str(pos1) + '.bmp'
            os.rename(os.path.join(path,file), os.path.join(path, new_name))
            print(new_name)
        elif file=='7.bmp':
            pos1 = pos
            new_name = '00000007_0' + str(pos1) + '.bmp'
            os.rename(os.path.join(path,file), os.path.join(path, new_name))
            print(new_name)
        elif file=='8.bmp':
            pos1 = pos
            new_name = '00000008_0' + str(pos1) + '.bmp'
            os.rename(os.path.join(path,file), os.path.join(path, new_name))
            print(new_name)
        elif file=='9.bmp':
            pos1 = pos
            new_name = '00000009_0' + str(pos1) + '.bmp'
            os.rename(os.path.join(path,file), os.path.join(path, new_name))
            print(new_name)
        elif file=='10.bmp':
            pos1 = pos
            new_name = '00000010_0' + str(pos1) + '.bmp'
            os.rename(os.path.join(path,file), os.path.join(path, new_name))
            print(new_name)

path = input("输入路径：")
pos = input("输入位置：")

rename_files(path,int(pos))


import os


def scan_files(dir, prefix=None, postfix=None):
    file_list = []
    for root, sub_dir, files in os.walk(dir):
        for special_file in files:
            if postfix:
                if special_file.endwith(postfix):
                    #file_list.append(os.path.join(root, special_file))
                    file_list.append(special_file)
            elif prefix:
                if special_file.startwith(prefix):
                    #file_list.append(os.path.join(root, special_file))
                    file_list.append(special_file)
            else:
                #file_list.append(os.path.join(root, special_file))
                file_list.append(special_file)
    return file_list

dirA = "e:\\code\\Practice"
file_list = scan_files(dirA)

for eachone in file_list:
    print(eachone)

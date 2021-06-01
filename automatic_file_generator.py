file_name = input("File name : ")
file_ext = input("File extention : ")
file_data = input("File data (optional) : ")
file_dest = input("File destination (optional / leave blanck to create at './') : ")
file = file_name+'.'+file_ext
file_path = file_dest+'/'+file
with open(file_path, 'w',encoding='utf-8') as fp:
    pass
    fp.write(file_data)
    if file_data == '':
        print(file+" created at "+file_dest+"/")
    else :
        print(file+" created at "+file_dest+"/ with data value : "+file_data)
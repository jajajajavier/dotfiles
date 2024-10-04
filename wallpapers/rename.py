import os
path = os.path.expanduser('~/Pictures/wallpapers/')

def rename_all(dir):
    files = os.listdir(dir)
    files.sort()

    cont = 0
    name_maxsize = len(str(len(files)))
    for i in range(len(files)):
        name_size = (len(str(i)))
        name = (name_maxsize - name_size) * '0' + str(i) + '.png'
        
        print(files[i] + ' : ', end='')

        if (files[i] == name):
            print('don\'t rename.')
        else:
            os.rename(dir+'/'+files[i], dir+'/'+name)
            print('renamed to ' + name)
            cont += 1;

    print ('  wallpapers    : ', len(files))
    print ('  total renamed : ', cont, end='\n\n\n\n')

def main():
    all_dirs = [path+i for i in os.listdir(path) if os.path.isdir(path+i)]

    for dir in all_dirs:
        print('selected directory : ', dir)
        rename_all(dir)

main()

import os, random, sys

def get_files():
    path = os.path.expanduser('~/Pictures/wallpapers/')
    all_dirs = [path+i for i in os.listdir(path) if os.path.isdir(path+i)]
    
    files = []
    for dir in all_dirs:
        files += [dir+'/'+f for f in os.listdir(dir)]
    
    return files

def set_wallpaper(file):
    try:
        os.system('feh --no-fehbg --bg-fill ' + file)
    except:
        print('error setting wallpaper with feh')

def set_lockscreen(file):
    try:
        os.system('betterlockscreen -u ' + file)
    except:
        print('error setting the lockscreen with betterlockscreen')

def main():
    try:
        selected = sys.argv[1]
    except:
        selected = random.choice(get_files())

    print('selected wallpaper : ', selected)

    print('setting wallpaper...')
    set_wallpaper(selected)
    
    print('setting lockscreen...')
    set_lockscreen(selected)

main()

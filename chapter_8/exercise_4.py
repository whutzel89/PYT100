import sys, os, time

def file_stat(file,stat):
    print('='*30)
    print('\tStats for for file: ',file)
    print('\tsize of file in bytes: ',stat.st_size)
    print('\tlast modified: ',time.ctime(stat.st_mtime))

if __name__ == "__main__":
    dir_name = sys.argv[1]
    size_file = sys.argv[2]
    files = [f for f in os.listdir(dir_name) if os.path.isfile(f)]
    for file in files:
        status = os.stat(file)
        if status.st_size >250:
            file_stat(file,status)

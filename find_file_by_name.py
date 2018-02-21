import os
import time

def findfile(start, name):
    '''
    find a specific filename and prints out the full path of matches
    '''
    for relpath, dirs, files in os.walk(start):
        # print(relpath, dirs, files)
        if name in files:
            full_path = os.path.join(start,relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))

def modified_within(top, seconds):
    '''
    find all files that have a recent modification time.
    '''
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            full_path = os.path.join(path, name)
            if os.path.exists(full_path):
                mtime = os.path.getmtime(full_path)
                if mtime > (now - seconds):
                    print(full_path)

if __name__ == '__main__':
    import sys
    # findfile(sys.argv[1], sys.argv[2])
    if len(sys.argv) != 3:
        print('Usage: {} dir seconds'.format(sys.argv[0]))
        raise SystemExit(1)
    modified_within(sys.argv[1], float(sys.argv[2]))
import sys
import os

def line_count(filepath):
    try:
        with open(filepath, "r") as f:
            return len(f.readlines())
    except:
        return -1    

def main():
    if len(sys.argv) < 2:
        print("Error: no folder path was given")
        return
    
    folder_path = sys.argv[1]
    if not os.path.exists(folder_path):
        print(f"Error: no folder path \"{folder_path}\"")
        return

    filenames = next(os.walk(folder_path), (None, None, []))[2]
    if "--recursive" in sys.argv or "-r" in sys.argv:
        for (dirpath, _, fnms) in os.walk(folder_path):
            dpath = dirpath.replace("\\", "/")
            if dpath != folder_path:
                for f in fnms:
                    filenames.append(f"{dpath}/{f}")
        
    
    file_extensions = list(filter(lambda a: a.startswith("."), sys.argv[2:]))
    if file_extensions:
        filenames = list(filter(lambda f: ("." + f.split(".")[-1]) in file_extensions, filenames))
    
    count = 0
    for file in filenames:
        if "/" not in file:
            file = folder_path + "/" + file
        c = line_count(file)
        count += c if c != -1 else 0

    print(f"Total line found of file types {file_extensions if file_extensions else '[All]'} --> {count} lines")

main()
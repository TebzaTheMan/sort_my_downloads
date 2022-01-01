import os
import shutil
import time
import sys
from pathlib import Path  
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# File extensions according to their folder type
folder_extensions = {
    'Documents' : ("doc","docx","html","htm","odt","pdf","xls","xlsx","ods","ppt","pptx","txt","csv","dotx","pgn"),
    'Images' : ("jpg","png","gif","webp","tiff","psd","raw","bmp","heif","indd","jpeg"),
    'Vector Images' : ("svg","ai","eps"),
    'Music' : ("mp3","m4a","aac","oga","flac","wav","pcm","aiff"),
    'Video' : ("webm","mpg","mp2","mpeg","mpe","mpv","ogg","mp4","m4p","m4v","avi","wmv","mov","qt","flv","swf","avchd"),
    'Compressed' : ("7z","arj","deb","pkg","rar","rpm","tar.gz","z","zip","tgz"),
    'Disc Images' : ("dmg","iso","toast","vcd"),
    'Executables' : ("apk","bat","bin","cgi","pl","exe","jar","msi","py","wsf","app"),
    'Fonts' : ("fnt","fon","otf","ttf"),
}
def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return str(Path.home() / "Downloads")

downloads_folder = get_download_path()

def get_only_files_in_dir ():
    print("getting files")
    files_only = []
    for filename in os.listdir(downloads_folder):
        file = f"{downloads_folder}/{filename}"
        if os.path.isfile(file):
            files_only.append(filename)
    return files_only

def create_folder(name):
    path =  os.path.join(downloads_folder,name)
    try:
        os.mkdir(path)
    except OSError:
        print(f"{name} folder already exists.")

def move_file (file_path,dest):
    if not os.path.exists(f"{dest}/{Path(file_path).name}"):
        try:
            shutil.move(file_path,dest)
        except shutil.Error as error:
            print(f"Error: {error}")

def sort_file(file_path):
    ext = os.path.splitext(file_path)[1][1:].lower()
    for folder_name , exts in folder_extensions.items():
        if ext in exts:
            dest = f"{downloads_folder}/{folder_name}"
            if os.path.exists(dest):
                move_file(file_path,dest)
            else:
                create_folder(folder_name)
                move_file(file_path,dest)
        else:
            other_folder = f"{downloads_folder}/Other"
            if os.path.exists(other_folder):
                move_file(file_path,other_folder)
            else:
                create_folder("Other")
                move_file(file_path,other_folder)


def sort_files(files):
    print("moving files")
    for filename in files:
        sort_file(f"{downloads_folder}/{filename}")
    print("Done")

def on_created(event):  
    sort_file(event.src_path)

def watch_files ():
    patterns = "*"
    ignore_patterns = [".DS_Store"]
    ignore_directories = True
    case_sensitive = True
    event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    event_handler.on_created = on_created
    event_handler.on_modified = on_created
    my_observer = Observer()
    my_observer.schedule(event_handler,downloads_folder)
    my_observer.start()

    print("Watching new files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        print(" Stopped watching files.")
    finally:
        my_observer.join()

def main():
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == "sort-and-watch":
            sort_files(get_only_files_in_dir())
            watch_files()
        elif action == "watch":
            watch_files()
        elif action =="sort":
            sort_files(get_only_files_in_dir())
        elif action == "help":
            print("Help \n") 
            print("sort-my-downloads sort - will sort your downloads ")
            print("sort-my-downloads watch - will only watch and sort new files you download")
            print("sort-my-downloads sort-and-watch - will start by sorting your downloads and start file watcher")
        else :
            print("Incorrect action requested.Type in 'sort-my-downloads help' for more information on how to use program.")
    else:
        sort_files(get_only_files_in_dir())

if __name__ == "__main__":
    main()
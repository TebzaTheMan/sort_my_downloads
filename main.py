import os
import shutil
import time
from pathlib import Path  
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

downloads_folder = "/users/Tebza/Desktop/test_folder"
directory = os.listdir(downloads_folder)

# File extensions according to their folder type
folder_extensions = {
    'Documents' : ("doc","docx","html","htm","odt","pdf","xls","xlsx","ods","ppt" "pptx","txt"),
    'Images' : ("jpg","png","gif","webp","tiff","psd","raw","bmp","heif","indd","jpeg"),
    'Vector Images' : ("svg","ai","eps","pdf"),
    'Music' : ("mp3","m4a","aac","oga","flac","wav","pcm","aiff"),
    'Video' : ("webm","mpg","mp2","mpeg","mpe","mpv","ogg","mp4","m4p","m4v","avi","wmv","mov","qt","flv","swf","avchd"),
    'Compressed' : ("7z","arj","deb","pkg","rar","rpm","tar.gz","z","zip"),
    'Disc Images' : ("dmg","iso","toast","vcd"),
    'Executables' : ("apk","bat","bin","cgi","pl","exe","jar","msi","py","wsf"),
    'fonts' : ("fnt","fon","otf","ttf"),
}

def get_only_files_in_dir ():
    print("getting files")
    files_only = []
    for filename in directory:
        file = "{}/{}".format(downloads_folder,filename)
        if os.path.isfile(file):
            files_only.append(filename)
    return files_only

files_only = get_only_files_in_dir()

def create_folder(name):
    path =  os.path.join(downloads_folder,name)
    try:
        os.mkdir(path)
    except OSError:
        print("{} folder already exists.".format(name))

def sort_file(filename):
    file_path = f"{downloads_folder}/{filename}"
    ext = os.path.splitext(filename)[1][1:].lower()
    for name , exts in folder_extensions.items():
        if ext in exts:
            if os.path.exists(f"{downloads_folder}/{name}"):
                try:
                    shutil.move(file_path,f"{downloads_folder}/{name}")
                except:
                    print(f"error occured while moving {filename} to folder {name}")
            else:
                create_folder(name)
                try:
                    shutil.move(file_path,f"{downloads_folder}/{name}")
                except:
                    print(f"error occured while moving {filename} to folder {name}")


def sort_files():
    print("moving files")
    for filename in files_only:
        sort_file(filename)
    print("Done")

sort_files()


def on_created(event):
    sort_file(Path(event.src_path).name)

if __name__ == "__main__":

    patterns = "*"
    ignore_patterns = [".DS_Store"]
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_event_handler.on_modified = on_created
    go_recursively = False  
    my_observer = Observer()
    my_observer.schedule(my_event_handler,downloads_folder, recursive=go_recursively)
    my_observer.start()

    print("Watching new files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        print("Stopped watching files.")
    my_observer.join() 


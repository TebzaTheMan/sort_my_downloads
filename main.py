import os
import shutil

downloads_folder = "/users/Tebza/Desktop/test_folder"
directory = os.listdir(downloads_folder)

# File extensions according to their folder  type
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

def get_all_file_extensions ():
    print("getting file extensions")
    found_exts = []
    for filename in files_only:
        ext = os.path.splitext(filename)[1][1:].lower()
        found_exts.append(ext)
    unique_exts = list(set(found_exts))
    return unique_exts

def create_folder(name):
    path =  os.path.join(downloads_folder,name)
    try:
        os.mkdir(path)
    except OSError:
        print("{} folder already exists.".format(name))

def create_needed_folders (extensions):
    print("creating folders")
    for ext in extensions:
        #get the object key that its value has the ext.
        for name , exts in folder_extensions.items():
            if ext in exts:
                create_folder(name)

def move_files():
    print("moving files")
    for filename in files_only:
        file = "{}/{}".format(downloads_folder,filename)
        ext = os.path.splitext(filename)[1][1:].lower()
        for name , exts in folder_extensions.items():
            if ext in exts:
                try:
                    shutil.move(file,"{}/{}".format(downloads_folder,name))
                except:
                    print("error occured while moving file {} to folder {}".format(filename, name))

create_needed_folders(get_all_file_extensions())
move_files()

print("Done")

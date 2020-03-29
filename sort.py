# -*- coding: utf-8 -*-
import argparse
import os
import shutil

''' This is a sorting scenario, which sort files in any CWD'''
''' 1) Get the path of the dir which will have been sorted
        path: str
    2) Create default folders from the dictionary below (dictionaries) '''


directories = {'Видео':         ["asf", "avi", "m1v", "mp2", "mp2v", "mpe", "mpeg", "mpg", "mpv2", "wm", "wmv", "mp4"],
               'Фото':          ["bmp", "dib", "emf", "gif", "jfif", "jpe", "jpeg", "jpg", "png", "tif", "tiff", "wmf", "heic"],
               'Аудио':         ["aif", "aifc", "aiff", "au", "mp2", "mp3", "mpa", "snd", "wav", "wma"],
               'Торрент-файлы': ["torrent"],
               'Книги и текстовые файлы':["docx", "txt", "pdf", "doc", "html", "rtf", "djvu", "epub", "mobi", "fb2", "xlsx"],
               'Python files':  ["py", 'pyw'],
               'Прочие файлы':  ['exe', "zip", 'bin', 'db', 'crdownload', 'rdf', "whl", 'msi', 'iso']
                }

def make_directory(path):
    # create dirs according to directories dict only once
    for key in directories.keys():
        new_directory = path + '\\' + key
        try:
            os.mkdir(new_directory)
        except:
            pass


def sortfiles(path):
    make_directory(path)
    # extract only extinctions
    for file in os.listdir(path):
        # check if it's fileobject
        if os.path.isfile(path + '\\' + file):
            #get the extinction of the file
            extinct = str(file).split('.')[-1]
            for folder in directories:
                if extinct in directories[folder]:
                    # get the current position of the file
                    current_file = path + '\\' + file
                    # get the destination to move
                    destination = path + '\\' + folder
                    # move all files to destination folder
                    try:
                        shutil.move(current_file, dst=destination)
                    except:
                        print('Done!')

if __name__ == '__main__':
    # if you need to sort exactly directory use <path> argument.
    try:
        parser = argparse.ArgumentParser(description = "Path argument parser")
        parser.add_argument("path", type=str, help='Path to sort')
        parser.add_argument("-a","--action", help='Usage: <your path to the directory to sort> -p/--path sort', default='sort')
        args = parser.parse_args()
        print(args)
        if args.action == "sort":
            sortfiles(args.path)
    except:
        path = os.path.normpath('C:\\Users\\user\\Documents\\Downloads')
        sortfiles(path)

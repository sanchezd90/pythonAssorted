import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS":['.pdf','.rft','.txt','.docx','.doc','.xlsx','.ppt'],
    "AUDIO":['.m4a','.m4b','.mp3'],    
    "VIDEOS":['.mov','.avi','.mp4','.m4v'],    
    "IMAGES":['.jpg','.jpeg','.png'],
    "SCRIPTS":['.py','.js']    
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"
print(pickDirectory('.pdf'))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() !=True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()
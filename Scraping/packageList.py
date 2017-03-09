from bs4 import BeautifulSoup
import json

#Function to find both occurences of a tag
def indices(string, substring):
    return [string.find(substring), string.find(substring) + string[string.find(substring) + 1:].find(substring)]

#Source Code File
file = open('/root/Desktop/GDG/PIP_GUI/Resource_Files/db.txt')
src = str(file.read())
file.close()

#List of all Genres and their 'a' tag HREF values
genreList = json.load(open('/root/Desktop/GDG/PIP_GUI/Resource_Files/genreListFile.j'))
genreTags = json.load(open('/root/Desktop/GDG/PIP_GUI/Resource_Files/genreTagFile.j'))

#Genre and HREF value dictionary
genres = json.load(open('/root/Desktop/GDG/PIP_GUI/Resource_Files/genreFile.j'))

#Tag values and their indices
indexDict = {i:max(indices(src, i)) for i in genreTags}

def substr(string, start, tag='ul'):
    sub = string[string[start:].find('<' + tag + '>')+start: string[start:].find('</' + tag + '>') + start + len('</' + tag + '>')]
    aTags = BeautifulSoup(sub, 'html.parser').find_all('a')
    return [i.string for i in aTags]

#Dictionary of genre tags with all relative packages
packageDict = {i:substr(src, indexDict[i]) for i in genreTags}

json.dump(packageDict, open('/root/Desktop/GDG/PIP_GUI/Resource_Files/packageDictFile.j', 'w'))

k = json.load(open('/root/Desktop/GDG/PIP_GUI/Resource_Files/packageDictFile.j'))
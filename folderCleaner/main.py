import os
import time


def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


if __name__ == '__main__':
    files = os.listdir()
    files.remove('main.py')
   # print(os.path.splitext(files[0]))
    # print(files)
    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')
    imgExts = [".png", ".jpg", ".jpeg"]
    docExts = ['.txt', '.docx', '.doc', '.pdf']
    medExts = ['.mp4', '.mp3']
    images = [file for file in files if os.path.splitext(file)[
        1].lower() in imgExts]
    docs = [file for file in files if os.path.splitext(file)[
        1].lower() in docExts]
    media = [file for file in files if os.path.splitext(file)[
        1].lower() in medExts]

    other = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in medExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            other.append(file)

    for img in images:
        os.replace(img, f"Images/{img}")
    for mds in media:
        os.replace(mds, f"Media/{mds}")
    move("Others", other)
    move("Docs", docs)
    # for doc in docs:
    #     os.replace(doc, f"Docs/{doc}")
    # for oth in other:
    #     os.replace(oth, f"Others/{oth}")
    # print(other)
    # print(images)
    # print(docs)
    # print(media)
    count = len(other) + len(images) + len(docs) + len(media)
    print(f"it cleared {count} files")

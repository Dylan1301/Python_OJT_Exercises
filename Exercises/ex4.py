pathList = ['/Users/viet_tran/Documents/applications.txt', '/Users/viet_tran/Documents/collections.txt',
'/Users/viet_tran/Documents/trainees.txt']

pathListClean = list(
    map( lambda x: x.split("/")[-1]\
        .split(".")[0].title(), pathList))

print(pathListClean)

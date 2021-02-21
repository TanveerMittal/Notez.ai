

def filter_vtt(data):
    names_count = dict()
    names_lines = dict()
    data = data.split("\n")
    data.pop(0)
    data.pop(0)
    try:
        while True:
            data.remove("")
    except:
        pass
    count=0
    for i in range(len(data)):
        if count%3==0 or count%3==1:
            data.pop(count//3)
        if count%3==2:
            data[count//3]=data[count//3].split(":")
            if len(data[count//3]) == 1:
                data[count//3]=""
            else:
                if data[count//3][0] not in names_count:
                    names_count[data[count//3][0]] = 0
                    names_lines[data[count//3][0]] = list()
                names_count[data[count//3][0]] += 1
                names_lines[data[count//3][0]].append(count//3)
                data[count//3]=data[count//3][1][1:]
        count+=1
    lecturer = None
    max = 0
    for n,c in names_count.items():
        if c > max:
            lecturer=n
            max=c

    to_remove=list()
    for n,l in names_lines.items():
        if n != lecturer:
            to_remove.extend(l)
    to_remove.sort(reverse=True)

    for i in to_remove:
        data.pop(i)

    try:
        while True:
            data.remove("")
    except:
        pass

    return " ".join(data)












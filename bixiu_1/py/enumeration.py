itemlist = ["低速低强度", "变速练习", "低速低强度", "快走", "低速低强度", "坡度练习", "低速低强度"]
datalist = [400, 600, 380, 0, 420, 620, 397]
finished = 0
unfinished = ""
for i in range(7):
    if datalist[i] == 0:
        unfinished = unfinished + itemlist[i] + " "
    else:
        finished = finished + 1
print("完成了", finished, "项")
print("未完成项目:", unfinished)
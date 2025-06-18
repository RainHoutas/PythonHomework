favorite_places = ["长城","故宫","西湖","长城"]

set_favorite_places = set(favorite_places)

if len(set_favorite_places) == len(favorite_places):
    print("没有重复的地方")
else:
    print("有重复的地方")
#先写一个列表，然后转换为集合，比较长度来判断是否有重复的地方
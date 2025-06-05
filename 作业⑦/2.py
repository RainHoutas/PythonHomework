def print_scenic_info(place, province, abbr):
    print(f"我最喜欢的景点是{place}")
    print(f"它位于{province}")
    print(f"{province}的简称是{abbr}")


info = {"place": "龙门石窟", "province": "河男省", "abbr": "与"}
print_scenic_info(**info)

#version_with_function

def loading_bar(insert_number):

    bar_progress = 0
    remain_progress = 0

    if random_num // 10 != 10:
        bar_progress = random_num // 10
        remain_progress = 10 - bar_progress
    else:
        bar_progress = 10

    if bar_progress != 10:
        print(f"{random_num}% [{bar_progress * chr(37)}{remain_progress * chr(46)}]")
        print(f"Still loading...")
    else:
        print("100% Complete!")
        print(f"[{bar_progress * chr(37)}{remain_progress * chr(46)}]")

    return bar_progress


random_num = int(input())

loading_bar(random_num)




#Version_without_funciton

# random_num = int(input())
#
# bar_progress = 0
# remain_progress = 0
#
# if random_num // 10 != 10:
#     bar_progress = random_num // 10
#     remain_progress = 10 - bar_progress
# else:
#     bar_progress = 10
#
#
# if bar_progress != 10:
#     print(f"{random_num}% [{bar_progress * chr(37)}{remain_progress * chr(46)}]")
#     print(f"Still loading...")
# else:
#     print("100% Complete!")
#     print(f"[{bar_progress * chr(37)}{remain_progress * chr(46)}]")


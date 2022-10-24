import os
import re

picPath = r'O:\任务\手势'
# pPath = r'O:\任务\手势\code'
matchPattern = r'IMG_(.*).MP4'
# matchPattern = r'p-IMG_4155.MP4'
rel_file_num = 4178
file_no = 55

filelist = os.listdir(picPath)

loop_pointer = rel_file_num
file_num_incre = 0

for i in range(0, len(filelist)) : 
    pic_name = filelist[i]
    # print(pic_name)
    #字符串操作，取出IMG_后面的数字
    matchObj = re.match(matchPattern, pic_name)
    # print(matchObj)
    if matchObj:
        cur_file_num = matchObj.group(1)
        if( int(cur_file_num) - loop_pointer == 1):
            file_num_incre += 1
            loop_pointer = int(cur_file_num)
            cor_file_num = file_no + file_num_incre
            if(cor_file_num - 100 < 0):
                cor_file_name = 'p0' + str(cor_file_num) + '-' + pic_name
            else:
                cor_file_name = 'p' + str(cor_file_num) + '-' + pic_name
            print("before correct:",pic_name," -> after correct:",cor_file_name)
            os.rename(picPath + "\\" + pic_name, cor_file_name)
            # print(picPath + "\\" + pic_name)
        else:
            loop_pointer = int(cur_file_num)
            print(cur_file_num, 'not continous:', pic_name)
            #要把修正pointer后的第一个标题也给改过来
            #file_no +file_num_incre + 1
            file_num_incre += 1
            cor_file_num = file_no + file_num_incre
            if(cor_file_num - 100 < 0):
                cor_file_name = 'p0' + str(cor_file_num) + '-' + pic_name
            else:
                cor_file_name = 'p' + str(cor_file_num) + '-' + pic_name
            print("before correct:",pic_name," -> after correct:",cor_file_name)
            os.rename(picPath + "\\" + pic_name, cor_file_name)
            continue

    else:
         continue


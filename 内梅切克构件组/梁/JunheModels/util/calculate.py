# -*- coding: utf-8 -*-
# @Time    : 2017/08/11
# @Author  : kingsley kuang
# @Site    : https://github.com/kingsley-gl/planbar.git
# @File    : Stirrup.py 箍筋文件
# @Software: 
# @Function: 




def steel_modify(total_length,diameter,distance,head_cover,end_cover):
    '''
    判断顶端根数修正函数
    '''
    end_pos = total_length - end_cover
    last_pos = int((total_length - head_cover - end_cover - diameter) / distance) * distance + head_cover
    print('end_pos',end_pos)
    print('last_pos',last_pos)
    if end_pos - last_pos < distance + diameter and end_pos - last_pos > distance / 2:
        return True
    else:
        return False

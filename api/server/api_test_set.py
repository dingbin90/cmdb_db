#!/usr/bin/env python
# -*- coding:utf-8 -*-
# a={1,2,3,4,5}
# b={4,5}
# c={5}


def get_in(*args):
    base=args[0]
    resalut = base.intersection(*args)
    return list(resalut)



def get_exclude(total,part):
    date = []
    for item in total:
        if item in part:
            pass
        else:
            date.append(item)
    return date
# if __name__ == "__main__":
#     _list = get_in(a,b,c)
#     print(_list)
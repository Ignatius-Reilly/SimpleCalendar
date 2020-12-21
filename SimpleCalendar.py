#!/usr/bin/env python3
r""" """

from sys import argv
import os
import subprocess as subp
import calendar as cal
import re


##CHECK
#Tal vez no definir 'kwargs = {}' y luego usar 'if kwargs'
#read optional arguments as **kwargs
kwargs = {}
if __name__=='__main__':
    if len(argv) >= 4:
        kwargs = dict(arg.split('=') for arg in argv[3:])

#Fields' values in the Latex template (list)
templ_dayNumber_keys = ['FD1-1','FD1-2','FD1-3','FD1-4','FD1-5','FD1-6','FD1-7',
                        'FD2-1','FD2-2','FD2-3','FD2-4','FD2-5','FD2-6','FD2-7',
                        'FD3-1','FD3-2','FD3-3','FD3-4','FD3-5','FD3-6','FD3-7',
                        'FD4-1','FD4-2','FD4-3','FD4-4','FD4-5','FD4-6','FD4-7',
                        'FD5-1','FD5-2','FD5-3','FD5-4','FD5-5','FD5-6','FD5-7',
                        'FD6-1','FD6-2'
                        ]

#Fields' values in the Latex template (dict)
templ_dayNumber_dic = {}
for key in templ_dayNumber_keys:
    templ_dayNumber_dic[key] = ''

#get list of weeks with lists of seven days.
def get_calendar(year, month):
    calendar = cal.Calendar()
    weeks = calendar.monthdayscalendar(year,month)
    weeks = [['' if x==0 else x for x in week] for week in weeks]
    return weeks

#replace values in text using dictionary:
def replace(rep_dict):
    """Thanks to Andrew Clark and others, from Stack overflow"""
    rep_dict = dict((re.escape(k), v) for k, v in rep_dict.items())
    pattern = re.compile("|".join(rep_dict.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)

weeks = get_calendar(int(argv[1]), int(argv[2]))
no_of_weeks = len(weeks)

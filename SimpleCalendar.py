#!/usr/bin/env python3
r""" """

from sys import argv
import os
import subprocess as subp
import calendar as cal
import re

#read optional arguments as **kwargs
kwargs = {}
if __name__=='__main__':
    if len(argv) >= 4:
        kwargs = dict(arg.split('=') for arg in argv[3:])

#Name of days
eng = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun',
       r'J\\A\\N\\U\\A\\R\\Y',r'F\\E\\B\\R\\U\\A\\R\\Y',r'M\\A\\R\\C\\H',
       r'A\\P\\R\\I\\L',r'M\\A\\Y',r'J\\U\\N\\E',r'J\\U\\L\\Y',
       r'A\\U\\G\\U\\S\\T',r'S\\E\\P\\T\\E\\M\\B\\E\\R',
       r'O\\C\\T\\O\\B\\E\\R',r'N\\O\\V\\E\\M\\B\\E\\R',
       r'D\\E\\C\\E\\M\\B\\E\\R']
eng_l = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',
         r'J\\A\\N\\U\\A\\R\\Y',r'F\\E\\B\\R\\U\\A\\R\\Y',r'M\\A\\R\\C\\H',
         r'A\\P\\R\\I\\L',r'M\\A\\Y',r'J\\U\\N\\E',r'J\\U\\L\\Y',
         r'A\\U\\G\\U\\S\\T',r'S\\E\\P\\T\\E\\M\\B\\E\\R',
         r'O\\C\\T\\O\\B\\E\\R',r'N\\O\\V\\E\\M\\B\\E\\R',
         r'D\\E\\C\\E\\M\\B\\E\\R']
esp = ['Lun','Mar','Mie','Jue','Vie','Sab','Dom',
       r'E\\N\\E\\R\\O',r'F\\E\\B\\R\\E\\R\\O',r'M\\A\\R\\Z\\O',
       r'A\\B\\R\\I\\L',r'M\\A\\Y\\O',r'J\\U\\N\\I\\O',R'J\\U\\L\\I\\O',
       r'A\\G\\O\\S\\T\\O',r'S\\E\\P\\T\\I\\E\\M\\B\\R\\E',
       r'O\\C\\T\\U\\B\\R\\E',r'N\\O\\V\\I\\E\\M\\B\\R\\E',
       r'D\\I\\C\\I\\E\\M\\B\\R\\E']
esp_l = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo',
         r'E\\N\\E\\R\\O',r'F\\E\\B\\R\\E\\R\\O',r'M\\A\\R\\Z\\O',
         r'A\\B\\R\\I\\L',r'M\\A\\Y\\O',r'J\\U\\N\\I\\O',R'J\\U\\L\\I\\O',
         r'A\\G\\O\\S\\T\\O',r'S\\E\\P\\T\\I\\E\\M\\B\\R\\E',
         r'O\\C\\T\\U\\B\\R\\E',r'N\\O\\V\\I\\E\\M\\B\\R\\E',
         r'D\\I\\C\\I\\E\\M\\B\\R\\E']
deu = ['Mo','Di','Mi','Do','Fr','Sa','So',
       r'J\\A\\N\\U\\A\\R',r'F\\E\\B\\R\\U\\A\\R',r'M\\Ä\\R\\Z',
       r'A\\P\\R\\I\\L',r'M\\A\\I',r'J\\U\\N\\I',r'J\\U\\L\\I',
       r'A\\U\\G\\U\\S\\T',r'S\\E\\P\\T\\E\\M\\B\\E\\R',
       r'O\\K\\T\\O\\B\\E\\R',r'N\\O\\V\\E\\M\\B\\E\\R',
       r'D\\E\\Z\\E\\M\\B\\E\\R']
deu_l = ['Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag',
         r'J\\A\\N\\U\\A\\R',r'F\\E\\B\\R\\U\\A\\R',r'M\\Ä\\R\\Z',
         r'A\\P\\R\\I\\L',r'M\\A\\I',r'J\\U\\N\\I',r'J\\U\\L\\I',
         r'A\\U\\G\\U\\S\\T',r'S\\E\\P\\T\\E\\M\\B\\E\\R',
         r'O\\K\\T\\O\\B\\E\\R',r'N\\O\\V\\E\\M\\B\\E\\R',
         r'D\\E\\Z\\E\\M\\B\\E\\R']

if 'lang' in kwargs:
    if kwargs['lang'] == 'eng':
        NoD = eng
    elif kwargs['lang'] == 'eng_l':
        NoD = eng_l
    elif kwargs['lang'] == 'esp':
        NoD = esp
    elif kwargs['lang'] == 'esp_l':
        NoD = esp_l
    elif kwargs['lang'] == 'deu':
        NoD = deu
    elif kwargs['lang'] == 'deu_l':
        NoD = deu_l
    else:
        NoD = eng
        print('Language ',kwargs['lang'],' is not supported')
else:
    NoD = eng

#-- Fields' values in the LaTeX template --
#Day numbers
templ_dayNumber_keys = ['FD1-1','FD1-2','FD1-3','FD1-4','FD1-5','FD1-6','FD1-7',
                        'FD2-1','FD2-2','FD2-3','FD2-4','FD2-5','FD2-6','FD2-7',
                        'FD3-1','FD3-2','FD3-3','FD3-4','FD3-5','FD3-6','FD3-7',
                        'FD4-1','FD4-2','FD4-3','FD4-4','FD4-5','FD4-6','FD4-7',
                        'FD5-1','FD5-2','FD5-3','FD5-4','FD5-5','FD5-6','FD5-7',
                        'FD6-1','FD6-2','FD6-X','FD6-X','FD6-X','FD6-X','FD6-X'
                        ]
templ_dayNumber_dic = {key:'' for key in templ_dayNumber_keys}

##TODO
#Day of the week
#DoW = {'Day1':'','Day2':'','Day3':'','Day4':'','Day5':'','Day6':'','Day7':''}
DoW = {'Day1':NoD[0],'Day2':NoD[1],'Day3':NoD[2],'Day4':NoD[3],
       'Day5':NoD[4],'Day6':NoD[5],'Day7':NoD[6]}

#Number of blocks in rows 1, 5 and 6
blocks_per_row = {'W1-H':'','W1-V':'','W5-H':'','W5-V':'','W6-H':'','W6-V':''}

#Month & Year
month_and_year = {'F-MONTH':NoD[int(argv[2])+6],
                  'F-YEAR': r'\\'.join([char for char in argv[1]])}

#Optional image in the background
background_image = {'CommentSymbol':r'%', 'BackgroundImage':''}

#All dictionaries about fields
field_dics = [templ_dayNumber_dic, DoW, blocks_per_row, background_image, month_and_year]

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

#Count number of days in a given week of the month
#i.e.: if the 1st week starts on Thu, day_counter(1stWeek) -> 4
def day_counter(week):
    return sum(type(day)==int for day in week)

weeks = get_calendar(int(argv[1]), int(argv[2]))
no_of_weeks = len(weeks)
no_of_days_week1 = day_counter(weeks[0])
if len(weeks) == 5:
    no_of_days_week5 = day_counter(weeks[4])
    no_of_days_week6 = 0
elif len(weeks) > 5:
    no_of_days_week5 = 7
    no_of_days_week6 = day_counter(weeks[5])
else:
    no_of_days_week5 = 0
    no_of_days_week6 = 0

blocks_per_row['W1-H'] = str(no_of_days_week1)
blocks_per_row['W1-V'] = str(no_of_days_week1 + (no_of_days_week1 != 0))
blocks_per_row['W5-H'] = str(no_of_days_week5)
blocks_per_row['W5-V'] = str(no_of_days_week5 + (no_of_days_week5 != 0))
blocks_per_row['W6-H'] = str(no_of_days_week6)
blocks_per_row['W6-V'] = str(no_of_days_week6 + (no_of_days_week6 != 0))

#Assign the right number to each day
unrolled_DoM = [day for week in weeks for day in week]
for day in range(len(unrolled_DoM)):
    templ_dayNumber_dic[templ_dayNumber_keys[day]] = str(unrolled_DoM[day])

#set a background image if requested
if 'image' in kwargs:
    background_image['CommentSymbol'] = ''
    background_image['BackgroundImage'] = kwargs['image']

#read template
with open('SimpleCalendar.tex') as template:
    almanac = template.read()

#Modify template
for dic in field_dics:
    for key in dic.keys():
        almanac = almanac.replace(key, dic[key])

#generates tex file
filename = 'SimpleCalendar_' + argv[1] + '_' + argv[2]
with open(filename+'.tex' ,'w') as file:
    file.write(almanac)

#print pdf file
subp.run(['pdflatex', filename+'.tex'])

#eliminate auxiliar files
if os.path.exists(filename+'.log'):
    os.remove(filename+'.log')
if os.path.exists(filename+'.aux'):
    os.remove(filename+'.aux')
if os.path.exists(filename+'.tex'):
    os.remove(filename+'.tex')

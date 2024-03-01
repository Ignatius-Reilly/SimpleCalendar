## Simple Calendar

Prints a grid with minimun design for a specified month and year in a pdf file.
Useful as a monthly planner, but can be easily upgraded to cover a whole year.

![Example](https://github.com/Ignatius-Reilly/SimpleCalendar/blob/main/Examples/Example1.png)

It requires Python 3 and pdflatex.

Language can be configured. Right now it supports:

* English
* Spanish
* German

but it's very easy to add another!!


### How to use it:

Both SimpleCalendar.py and the LaTeX template SimpleCalendar.tex should be in the same folder.
Make sure SimpleCalendar.py has permission for execution.
Then just call it as
```
./SimpleCalendar.py YYYY MM
```

To change language:
```
./SimpleCalendar.py YYYY MM lang=<language>
```

The languages supported in the current version are:
* `eng` (deafualt): Mon Tue...
* `eng_l`: Monday Tuesday...
* `esp`: Lun Mar...
* `esp_l`: Lunes Martes...
* `deu`: Mo Di...
* `deu_l`: Montag Dienstag...

Default language can be easily changed in the source code.

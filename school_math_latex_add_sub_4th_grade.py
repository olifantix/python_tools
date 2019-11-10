import random
import re
import os
import subprocess

latex_inner_inner_template = r"""\begin{array}{lr}
 & %%%0%%% \\
%%%2%%% & %%%1%%% \\
&\\
\hline
&\qquad 
\end{array}\qquad
"""

latex_inner_template = r"""\[
\huge 
\begin{array}{cccc}
%1
%%%0%%%
%2
%%%1%%%
%3
%%%2%%%
%4
%%%3%%%
\end{array}
\]

"""

latex_template_head = r"""
\documentclass[14pt,a4paper,sans, final]{article}  
\usepackage[ngerman]{babel}
\usepackage{pdfpages}
\usepackage[scale=0.75]{geometry} % Reduce document margins

\begin{document}

"""

latex_template_foot = r"""

\end{document}
"""

def task(minimum, maximum, s = None):
    def mm(a,b):
       return (a,b) if a>b else (b,a)
    r = -1
    s = s or random.choice([1,-1])
    while not minimum <= r <= maximum:
        a,b = mm(random.choice(range(40,10001)), random.choice(range(40,10001)))
        r = a + s*b

    return (a,b,'+' if s==1 else '-')

def getName():
    p = "task{}.tex"
    k = 0
    while True:
        name = p.format("" if k == 0 else k)
        if not os.path.isfile(name):
            break
        else: 
            k += 1
    return name


pp = 24
tasks = [task(57, 9999, 1) for _ in range(pp//2)]
tasks.extend( [task(57, 9999, -1) for _ in range(int(pp*1.5//1))] )

random.shuffle(tasks)

lines = 5
parts = [ tasks[i:i+4] for i in range(0,lines*4,4)] 


def make_one(data):
    # data  [(6774, 3588, '-'), (3714, 2183, '-'), (6018, 1168, '-'), (1430, 83, '-')]
    s = []
    for d in data:
        a,b,c = map(str,d)
        s.append(latex_inner_inner_template.replace("%%%0%%%",a).replace("%%%1%%%",b).replace("%%%2%%%",c))
    return latex_inner_template.replace("%%%0%%%",s[0]).replace("%%%1%%%",s[1]).replace("%%%2%%%",s[2]).replace("%%%3%%%",s[3])

filename = getName()
filenameprefix = filename.split(".")[0]
with open(filename ,"w") as fff:
    fff.write(latex_template_head) 
    for idx,p in enumerate(parts): 
        fff.write( make_one(p))

    fff.write(latex_template_foot)


pdfLatex = r"C:\Program Files\MiKTeX 2.9\miktex\bin\x64\pdflatex.exe"
acrReader = r"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"

cmd = [pdfLatex, '-interaction', 'nonstopmode', filename]
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink(filename)
else:
    cmd = [acrReader, f'{filenameprefix}.pdf']
    proc = subprocess.Popen(cmd)
    proc.communicate()

os.unlink(f'{filenameprefix}.log')

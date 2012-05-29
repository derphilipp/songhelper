import string


def writehead():
    return r"""\documentclass{article}
\usepackage[german]{babel}
\usepackage[a4paper,vmargin={2mm,2mm},hmargin={2mm,2mm}]{geometry}
\usepackage{fontspec}
\usepackage[chorded]{songs}
\newindex{titleidx}{titleidx}
\noversenumbers
\begin{document}
\begin{songs}{titleidx}
\beginsong{Songtitle}[by={Author}]
\beginverse

"""

def writeend():
    return r"""

\endverse
\endsong
\end{songs}
\end{document}
"""

def mergeline(chords, song):
    t_chords = chords.split()
    while t_chords:
        c = t_chords[-1]
        position = chords.rfind(c)
        song = song[:position] + "\\[" + c + "]" + song[position:]
        t_chords = t_chords[:-1]
    return song


def ischordline(txt):
    l=txt.split()
    amount = len(l)
    m = 0
    for i in l:
        m+=len(i)
    mins = m / amount
    if mins<3:
        return True


read = open("input.txt", "r")
write = open("output.tex","w")
outputtext = []

for i in read:
    if string.strip(i) == "":
        pass
    else:
        outputtext.append(string.strip(i).replace("&","\&").replace("%","\%").replace("...","\dots"))

chordline = ""
textline  = ""

write.write(writehead())

l = len(outputtext)
for i in range(0,l):
    r = outputtext[i]
    if ischordline(r):
        chordline = r
    else:
        textline = r
        write.write("\n")
        write.write(mergeline(chordline,textline))
        chordline=""
        textline=""
write.write(writeend())

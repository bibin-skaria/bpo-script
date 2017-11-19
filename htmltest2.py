import csv
# function to replace character and add space in file
def myfunc(line):
    b = line.replace(';', "&#59; ")
    c = b.replace('-', "&#45;")
    d = c.replace(':', "&#58; ")
    e = d.replace('.', "&#39;  ")
    f = e.replace(',', "&#44; ")
    g = f.replace('(', " &#40;")
    h = g.replace(')', "&#41; ")
    i = h.replace('/', "&#47;")
    j = i.replace(':', "&#58; ")
    h1 = j.replace('<', " &#60;")
    k1 = h1.replace('>', "&#62; ")
    l1 = k1.replace('\\', "&#47;")
    m1 = l1.replace('_', "&#95;")
    n1 = m1.replace('!', "&#33; ")
    o1 = n1.replace("+", " &#43; ")
    p1 = o1.replace('“', " &ldquo;")
    q1 = p1.replace('”', "&rdquo; ")
    r1 = q1.replace('‘', " &lsquo;")
    s1 = r1.replace('’', "&rsquo; ")

    y = 0
    y2 = 0
    n = ""
    for k in s1:
        if k == '"' and y == 0:
            m = k.replace('"', ' &ldquo;')
            n += m
            y = 1

        elif k == '"' and y == 1:
            m = k.replace('"', '&rdquo; ')
            n += m
            y = 0
        elif k == '\'' and y2 == 0:
            m = k.replace('\'', ' &lsquo;')
            n += m
            y2 = 1
        elif k == '\'' and y2 == 1:
            m = k.replace('\'', '&rsquo; ')
            n += m
            y2 = 0
        elif k == "+":
            m = k.replace("+", " &#43; ")
            n += m
            y2 = 0
        else:
            n += k
    o = n
    pr = o.replace('bak', ' ')
    return pr

SOURCE_FILE = './Liner2.csv'
DEST_FILE = './ebin12.txt'
with open(DEST_FILE,'w') as dst_file:
      with open(SOURCE_FILE) as src_file:
            readCSV = csv.reader(src_file, delimiter=',')
            a=0
            for line in readCSV:
                dst_file.write("<doctypehtml" + str(a) + ">\n""<html>\n""<body>\n" + myfunc(line[1]) + "\n" + myfunc(
                    line[2]) + "\n" + myfunc(line[3]) + "\n" + myfunc(line[4]) + "\n""</body>\n""</html>\n")
                # dst_file.write("&#60;doctypehtml" + str(a) + "&#62;\n""&#60;html&#62;\n""&#60;body&#62;\n" + oo + "\n" + ooo + "\n" + o + "\n" + oooo + "\n""&#60;&#47;body&#62;\n""&#60;&#47;html&#62;\n")
                a = a + 1

#remove top 9 unwanted lines
File = './ebin12.txt'
lines = open(File).readlines()
open('./ebin12.txt','w').writelines(lines[9:-1])
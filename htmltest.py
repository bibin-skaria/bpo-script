import csv
SOURCE_FILE = './Liner2.csv'
DEST_FILE = './ebin10.txt'
with open(DEST_FILE,'w') as dst_file:
      with open(SOURCE_FILE) as src_file:
            readCSV = csv.reader(src_file, delimiter=',')
            a=0
            for line in readCSV:
                b = line[3].replace(';',"&#59;bak")
                c = b.replace('-',"&#45;")
                d = c.replace(':',"&#58;bak")
                e = d.replace('.',"&#39;bakbak")
                f = e.replace(',',"&#44;bak")
                g = f.replace('(',"bak&#40;")
                h = g.replace(')',"&#41;bak")
                i = h.replace('/',"&#47;")
                j = i.replace(':',"&#58;")
                h1 = j.replace('<',"bak&#60;")
                k1 = h1.replace('>',"&#62;bak")
                l1 = k1.replace('\\',"&#47;")
                m1 = l1.replace('_',"&#95;")
                n1 = m1.replace('!',"&#33;bak")
                o1 = n1.replace("+","&#43;")
                p1 = o1.replace('“',"bak&ldquo;")
                q1 = p1.replace('”',"&rdquo;bak")
                r1 = q1.replace('‘',"bak&lsquo;")
                s1 = r1.replace('’',"&rsquo;bak")

                y = 0
                y2 = 0
                n = ""
                for k in s1:
                 if k == '"' and y == 0:
                    m = k.replace('"','bak&ldquo;')
                    n += m
                    y = 1

                 elif k == '"' and y == 1:
                    m = k.replace('"','&rdquo;bak')
                    n += m
                    y = 0
                 elif k== '\'' and y2 == 0:
                    m=k.replace('\'','bak&lsquo;')
                    n += m
                    y2 = 1
                 elif k == '\'' and y2 == 1:
                    m = k.replace('\'', '&rsquo;bak')
                    n += m
                    y2 = 0
                 elif k == "+":
                    m = k.replace("+", "bak&#43;bak")
                    n += m
                    y2 = 0
                 else:
                    n += k
                o = n
                pr = o.replace ('bak',' ')
                bb = line[1].replace(';', "&#59;")
                cc = bb.replace('-', "&#45;")
                dd = cc.replace(':', "&#58;bak")
                ee = dd.replace('.', "&#39;bakbak")
                ff = ee.replace(',', "&#44;bak")
                gg = ff.replace('(', "bak&#40;")
                hh = gg.replace(')', "&#41;bak")
                ii = hh.replace('/', "&#47;")
                jj = ii.replace(':', "bak&#58;")
                h2 = jj.replace('<', "bak&#60;")
                k2 = h2.replace('>', "&#62;bak")
                l2 = k2.replace('\\', "&#47;")
                m2 = l2.replace('_', "&#95;")
                n2 = m2.replace('!', "&#33;bak")
                o2 = n2.replace("+", "&#43;")
                p2 = o2.replace('“', "bak&ldquo;")
                q2 = p2.replace('”', "&rdquo;bak")
                r2 = q2.replace('‘', "bak&lsquo;")
                s2 = r2.replace('’', "&rsquo;bak")
                yy = 0
                yy2 = 0
                nn = ""

                for kk in s2:
                 if kk == '"' and yy == 0:
                    mm = kk.replace('"', 'bak&ldquo;')
                    nn += mm
                    yy = 1
                 elif kk == '"' and yy == 1:
                    mm = kk.replace('"', '&rdquo;bak')
                    nn += mm
                    yy = 0
                 elif kk == '\'' and yy2 == 0:
                    mm = kk.replace('\'', 'bak&lsquo;')
                    nn += mm
                    yy2 = 1
                 elif kk == '\'' and yy2 == 1:
                    mm = kk.replace('\'', '&rsquo;bak')
                    nn += mm
                    yy2 = 0
                 elif kk == "+":
                     mm = kk.replace("+", "bak&#43;bak")
                     nn += mm
                     yy2 = 0
                 else:
                    nn += kk
                oo = nn
                pr1 = oo.replace('bak', ' ')
                bbb = line[2].replace(';',"&#59;bak")
                ccc = bbb.replace('-', "&#45;")
                ddd = ccc.replace(':', "&#58;bak")
                eee = ddd.replace('.', "&#39;bakbak")
                fff = eee.replace(',', "&#44;bak")
                ggg = fff.replace('(', "bak &#40;")
                hhh = ggg.replace(')', "&#41;bak")
                iii = hhh.replace('/', "&#47;")
                jjj = iii.replace(':', "&#58;bak")
                h3 = jjj.replace('<', "bak&#60;")
                k3 = h3.replace('>', "&#62;bak")
                l3 = k3.replace('\\', "&#47;")
                m3 = l3.replace('_', "&#95;")
                n3 = m3.replace('!', "&#33;bak")
                o3 = n3.replace("+", "&#43;")
                p3 = o3.replace('“', "bak&ldquo;")
                q3 = p3.replace('”', "&rdquo;bak")
                r3 = q3.replace('‘', "bak&lsquo;")
                s3 = r3.replace('’', "&rsquo;bak")
                yyy = 0
                yyy2= 0
                nnn = ""
                for kkk in s3:
                 if kkk == '"' and yyy == 0:
                  mmm = kkk.replace('"',"bak&ldquo;")
                  nnn += mmm
                  yyy = 1
                 elif kkk == '"' and yyy == 1:
                  mmm = kkk.replace('"','&rdquo;bak')
                  nnn += mmm
                  yyy = 0
                 elif kkk== '\'' and yyy2 == 0:
                  mmm=kkk.replace('\'','bak&lsquo;')
                  nnn += mmm
                  yyy2 = 1
                 elif kkk== '\'' and yyy2 == 1:
                  mmm = kkk.replace('\'','&rsquo;bak')
                  nnn += mmm
                  yyy2 = 0
                 elif kkk == "+":
                  mmm = kkk.replace("+", "bak&#43;bak")
                  nnn += mmm
                  yyy2 = 0
                 else:
                  nnn += kkk
                ooo = nnn
                pr2 = ooo.replace('bak', ' ')
                bbbb = line[4].replace(';',"&#59;bak")
                cccc = bbbb.replace('-',"&#45;")
                dddd = cccc.replace(':',"&#58;bak")
                eeee = dddd.replace('.',"&#39;bak")
                ffff = eeee.replace(',',"&#44;bak")
                gggg = ffff.replace('(',"bak&#40;")
                hhhh = gggg.replace(')',"&#41;bak")
                iiii = hhhh.replace('/',"&#47;")
                jjjj = iiii.replace(':',"&#58;bak")
                h4 = jjjj.replace('<',"bak&#60;")
                k4 = h4.replace('>',"&#62;bak")
                l4 = k4.replace('\\',"&#47;")
                m4 = l4.replace('_',"&#95;")
                n4 = m4.replace('!',"&#33;bak")
                o4 = n4.replace("+","&#43;")
                p4 = o4.replace('“',"bak&ldquo;")
                q4 = p4.replace('”',"&rdquo;bak")
                r4 = q4.replace('‘',"bak&lsquo;")
                s4 = r4.replace('’',"&rsquo;bak")


                yyyy = 0
                yyyy2 = 0
                nnnn = ""

                for kkkk in jjjj:

                 if kkkk == '"' and yyyy == 0:
                  mmmm = kkkk.replace('"', 'bak&ldquo;')
                  nnnn += mmmm
                  yyyy = 1

                 elif kkkk == '"' and yyyy == 1:
                  mmmm = kkkk.replace('"', '&rdquo;bak')
                  nnnn += mmmm
                  yyyy = 0
                 elif kkkk == '\'' and yyyy2 == 0:
                  mmmm = kkkk.replace('\'', 'bak&lsquo;')
                  nnnn += mmmm
                  yyyy2 = 1
                 elif kkkk == '\'' and yyyy2 == 1:
                  mmmm = kkkk.replace('\'', '&rsquo;bak')
                  nnnn += mmmm
                  yyyy2 = 0
                 elif kkkk == "+":
                  mmmm = kkkk.replace("+", "bak&#43;bak")
                  nnnn += mmmm
                  yyyy2 = 0
                 else:
                  nnnn += kkkk

                oooo = nnnn
                pr3 = oooo.replace('bak', ' ')
                dst_file.write("<doctypehtml" + str(a) + ">\n""<html>\n""<body>\n" + pr1 + "\n" + pr2 + "\n" + pr + "\n" + pr3 + "\n""</body>\n""</html>\n")
                #dst_file.write("&#60;doctypehtml" + str(a) + "&#62;\n""&#60;html&#62;\n""&#60;body&#62;\n" + oo + "\n" + ooo + "\n" + o + "\n" + oooo + "\n""&#60;&#47;body&#62;\n""&#60;&#47;html&#62;\n")
                a = a + 1
# to remove unwanted field
File = './ebin10.txt'
lines = open(File).readlines()
open('./ebin11.txt','w').writelines(lines[9:-1])
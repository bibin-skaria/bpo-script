# regulare expression for spaceing rules
import re


def myfunc(line):

    b = re.sub('&#59;  ','&#59; ',line)
    c = re.sub('&#58;  ', '&#58; ', b)
    d = re.sub('&#8901;  ', '&#8901; ', c)
    e = re.sub('&#44;  ', '&#44; ', d)
    f = re.sub('  &#40;', ' &#40;', e)
    e = re.sub('&#41;  ', '&#41; ', f)
    g = re.sub('&#58;  ', '&#58; ', e)
    h = re.sub('  &#60;', ' &#60;', g)
    i = re.sub('&#62;  ', '&#62; ', h)
    j = re.sub('&#33;  ', '&#33; ', i)
    k = re.sub('&#43;  ', '&#43; ', j)
    l = re.sub('  &#43;', ' &#43;', k)
    m = re.sub('  &ldquo;', ' &ldquo;', l)
    n = re.sub('&rdquo;  ', '&rdquo; ', m)
    o = re.sub('  &lsquo;', ' &lsquo;', n)
    p = re.sub('&rdquo;  ', '&rdquo; ', o)

    return p

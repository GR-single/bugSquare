

def isyoubian(a):
    for x in a:
        if x.frb.right==600:
            return False
    return True
def iszuobian(a):
    for x in a:
        if x.frb.left==0:
            return False
    return True
def isxiabian(a):
    for x in a:
        if x.frb.bottom==600:
            return False
    return True
def peng(a,b):
    for x in a:
        for y in b:
            if x.frb.bottom==y.frb.top and x.frb.left==y.frb.left:
                return False
    return True
def lineyd(l):
    for f in l:
        f.ydxia(30) 
def zuopeng(a,b):
    for l in b:
        for f in l:
            for h in a:
                if h.frb.left==f.frb.right and h.frb.bottom==f.frb.bottom:
                    return False
    return True
def youpeng(a,b):
    for l in b:
        for f in l:
            for h in a:
                if h.frb.right==f.frb.left and h.frb.bottom==f.frb.bottom:
                    return False
    return True



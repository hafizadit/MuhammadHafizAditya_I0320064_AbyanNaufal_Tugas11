import math

def l_persegipanjang(p,l):
    return p * l

def k_persegipanjang(p,l):
    return 2 * (p + l)

def l_bujursangkar(s):
    return s * s

def k_bujursangkar(s):
    return 4 * s

def l_lingkaran(r):
    return math.pi * (r ** 2)

def k_lingkaran(r):
    return 2 * math.pi * r

def l_segitiga(a,t):
    return 0.5 * a * t

def k_segitiga(a,b,c):
    return a + b + c
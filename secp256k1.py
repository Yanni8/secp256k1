"""
© Yanni8 https://github.com/Yanni8
This algorythmus is not efficient and also probaly not 100% secure. 
Attackers could use Timing Attack (https://en.wikipedia.org/wiki/Timing_attack) to get informations about the private key 
"""

A = 0
B = 7
P = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
GX = 55066263022277343669578718895168534326250603453777594175500187360389116729240
GY = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (GX, GY)

def point_add(p1 : tuple, p2 : tuple) -> tuple:
    if p1 != p2:
        lam = (p1[1] - p2[1]) * pow(p1[0] - p2[0], P-2, P)
        x3 = (pow(lam, 2) - p1[0] - p2[0]) % P
        y3 = (lam * (p1[0] - x3) - p1[1])  % P
        return (x3, y3)
    return point_dubl(p1)

def point_dubl(p1 : tuple) -> tuple:
    lam = (3*p1[0]**2 + A) * pow(2*p1[1], P-2, P)
    v = p1[1] - lam*p1[0] % P
    x3 = (lam**2 - 2*p1[0]) % P
    y3 = (lam*x3 + v) * -1 % P
    return (x3, y3)


def calc_publ(private_key):
    publ = None
    Q = G
    binar = private_key
    while binar:
        if binar%2 == 1:
            if publ == None:
                publ = Q
            else:
                publ = point_add(publ, Q)
        Q = point_dubl(Q)
        binar = binar//2    
    return publ  

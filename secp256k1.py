"""
© Yanni8 https://github.com/Yanni8
"""

a = 0
b = 7 
p = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (Gx, Gy)


def point_add(p1 : tuple, p2 : tuple) -> tuple:
    if p1 != p2:
        lam = (p1[1] - p2[1]) * pow(p1[0] - p2[0], -1, p)
        x3 = (pow(lam, 2) - p1[0] - p2[0]) % p
        y3 = (lam * (p1[0] - x3) - p1[1]) % p
        return (x3, y3)
    return point_dubl(p1)

def point_dubl(p1 : tuple) -> tuple:
    print(p1[1])
    lam = (3*p1[0]**2 + a) * pow(2*p1[1], -1, p)
    v = p1[1] - lam*p1[0] % p
    x3 = (lam**2 - 2*p1[0]) % p
    y3 = (lam*x3 + v) * -1 % p
    return (x3, y3)


def calc_publ(private_key):
    publ = (Gx, Gy)
    Q = (Gx, Gy)
    binar = bin(private_key)
    while binar:
        Q = point_dubl(Q)
        if binar%2 == 1:
            publ = point_add(publ, Q)
        binar = binar//2    
    return publ  


def example_test():
    private_key = "0x69"
    publ = calc_publ(private_key)
    print(publ)
    assert publ == (0xf219ea5d6b54701c1c14de5b557eb42a8d13f3abbcd08affcc2a5e6b049b8d63,
                    0x4cb95957e83d40b0f73af4544cccf6b1f4b08d3c07b27fb8d8c2962a400766d1)

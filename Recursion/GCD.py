def gcd(a,b) : 
    isinstance(a,int) and isinstance(b, int) , "please enter a valid two positive integers"
    if a < 0 :
        a = -1 * a;
    if b < 0 :
        b = -1 * b;
    if (b == 0) :
        return a
    return gcd(b, a % b)

print(gcd(48,-18))


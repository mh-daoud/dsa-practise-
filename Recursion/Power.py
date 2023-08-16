def power(base,n) :
    assert n > -1 and isinstance(n,int) , "please enter a positive integer as the power"
    if( n == 1) :
        return base;
    if(n == 0) :
        return 1;
    return base * power(base , n - 1)

print(power(212,4))
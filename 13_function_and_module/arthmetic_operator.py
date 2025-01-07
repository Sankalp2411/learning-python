def add(a,b,*args):
    c = a + b + sum(args);
    return c;
def sub(a,b):
    c = a-b;
    return c;
def mul(a,b,*args):
    c = a*b*mul(args);
    return c;
def div(a,b):
    c=a/b;
    return c;
def print_kwargs(**kwargs): #kwargs : keywordargument, ** : 키벨류
    print(kwargs)
    print(kwargs['a'])
    print(kwargs['b'])
    
print_kwargs(a=1,b=2)
    
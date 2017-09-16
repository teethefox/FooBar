def FooBar():
  for target in range(100,100001):
    prime = True
    perfSqr = False
    for num in range(2,target+1):
        if target % num == 0 and num != target:
            prime = False

        if target // num == num:
            perfSqr = True

    if prime is True:
        print 'Foo'
    elif perfSqr is True:
        print 'Bar'
    else:
        print 'FooBar'
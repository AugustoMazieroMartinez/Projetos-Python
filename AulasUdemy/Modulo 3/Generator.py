def generator(n=0):
    yield 8
    return 'acabou'

gen = generator(n=0)
print(next(gen))
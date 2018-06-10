
def take(count,iterable):
    counter=0
    for item in iterable:
        if counter == count:
            return
        counter +=1
        yield item


def run_take():
    items = [2,5,4,6,9,8]
    for item in take(4,items):
        print(item)


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    items = [55,77,55,88,99,55,77,66]
    for item in distinct(items):
        print(item)



def run_pipeline():
    items = [3,1,1,2,6,6,5]
    for item in take(3,distinct(items)):
        print(item)


if __name__ == "__main_":
    run_pipeline()



#
# if __name__ == "__main__":
#     run_distinct()


# if __name__ == "__main__":
#     run_take()

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a,b = b, a+b



y = lucas()
for x in range(10):
    print(next(y))


# Generator Comprehension

gener =  (x*x for x in range(1,10))
print(gener)

print(list(gener))
print(list(gener))

gener =  [x*x for x in range(1,10)]
print(gener)
print(gener)

z=sum(x*x for x in range(1,1000001))
print(z)


ff = 'police'
print(ff.title())

a = [1,2,5,3,4,5,6,8,9,4,5,3]
b = [9,8,5,6,2,]

print(list(zip(a,b)))
for mo,ca in zip(a,b):
    print(sum([mo,ca]))

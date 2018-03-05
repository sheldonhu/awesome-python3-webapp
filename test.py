def reverse(data):
    for index in range(len(data)-1, -1, -1):
        print(index)
        yield data[index]

def main(data):
    for c in reverse(data):
        print(c)

g = (x for x in range(10))
r=g.send(None)
print(r)
if __name__ == '__main__':
    data = 'fdsafdsl'
    #main(data)
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def __call__(self):
        print('this is a callable object')

c = Chain()

if callable(c):
    c()
else:
    pass

# print(Chain().status.user.timeline.list)
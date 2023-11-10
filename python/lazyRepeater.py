def make_looper(string):
    def loop():
        for character in string:
            yield character
    return loop

def make_looper1(string):
    it = iter(string)
    yield next(it)

if __name__ == "__main__":
    # abc = make_looper1("abc")
    m



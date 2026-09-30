def mytest(value):
    if value == "foo":
        return True
    return None

class TestModule(object):
    def tests(self):
        return { 'foo_string': mytest }

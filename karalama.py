from functools import wraps

def logger(func):
    @wraps(func)
    def logging(*args, **kwargs):
        print(func.__name__ + " was called with following parameters.", args, kwargs)
        return func(*args, **kwargs)
    return logging

@logger
def test(name):
    "This is the test function."
    return name

print(test(name="Erdem"), test.__doc__)


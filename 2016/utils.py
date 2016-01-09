from functools import wraps

def memo(func):
    """ Memoisation decorator.
        from: Hetland, Python Algorithms, 2nd edition.

        usage:

        @memo
        def fib(i):
            if i < 2: return 1
            return fib(i-1) + fib(i-2)
    """
    cache = {}                          # Stored subproblem solutions
    @wraps(func)                        # Make wrap look like func
    def wrap(*args):                    # The memoized wrapper
        if args not in cache:           # Not already computed?
            cache[args] = func(*args)   # Compute & cache the solution
        return cache[args]              # Return the cached solution
    return wrap                         # Return the wrapper

def logger(func):
    """ Decorator that prints function calls and return values
        adapted from:
        http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
    """
    def inner(*args, **kwargs): #1
        print "*** %s(): Called with: %s, %s" % (func.__name__, args, kwargs)
        ret = func(*args, **kwargs) #2
        print "*** %s(): Returns: %s" % (func.__name__, ret)
        return ret
    return inner

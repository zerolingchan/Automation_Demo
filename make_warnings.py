import warnings

def make_warn():
    warnings.warn("deprecated", DeprecationWarning)

def not_warn():
    pass
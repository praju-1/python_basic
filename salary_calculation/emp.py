
def hra(basic):
    "This function return value house rent allowance"
    hra = basic * 0.15
    return hra

def ta(basic):
    "This function return value travells allowance"
    ta = basic * 0.10
    return ta

def pf(basic):
    "This function return value of provident fund"
    pf = basic * 0.12
    return pf

def itax(gross):
    "This function return value of tax to be paid"
    itax = gross * 0.05
    return itax
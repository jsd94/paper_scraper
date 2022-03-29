from math import log10

def null(arg):
    return arg

def is_quality(text):
    if text == '':
        return False
    else:
        bad_reads = 0
        for char in text:
            if char == '\uFFFD':
                bad_reads+=1
        if 1.0*bad_reads/len(text) > 0.1:
            return False
        else:
            return True

def percent_decrease_to_lrv(percent_decrease):
    return log10(100/(100-percent_decrease))
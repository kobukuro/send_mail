import sys
import linecache

def get_exception_message():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    global lineno
    lineno = tb.tb_lineno
    global filename
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    global error_text
    error_text = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    error_text = error_text[:3950]
    return error_text
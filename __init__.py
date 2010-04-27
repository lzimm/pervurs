import MySQLdb
from MySQLdb.cursors import DictCursor

conn = MySQLdb.connect(user="qorporation", db="pervurs")

def db():
    try:
        conn.ping()
        return conn.cursor(DictCursor)
    except:
        conn = MySQLdb.connect(user="qorporation", db="pervurs")
        return conn.cursor(DictCursor)

def import_mod(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

def import_comp(mod, comp):
    mod = __import__(mod, globals(), locals(), [comp])
    return getattr(mod, comp)
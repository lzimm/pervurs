import simplejson as json

from pervurs.models.aux.search import SearchSuggestion

def http(req):
    q = req.args.get('q', [""])[0]
    
    res = [s.suggestion for s in SearchSuggestion.filter(suggestion__like=q, order_by="frequency", order_dir="DESC").fetchall()]
    
    req.output = json.dumps(res)
    
    return None
    
    
    
    
def http(req):    
    post_filter = req.settings.ref.posts.filter(order_by="posted", limit=req.args.get('limit', [10])[0], offset=req.args.get('page', [0])[0])
    req.posts = post_filter.fetchall(count=True)
    req.pagination = post_filter
    
    return None
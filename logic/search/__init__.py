from pervurs.deps.sphinxapi import *
from pervurs.models import Post
from pervurs.includes.urls import links
from pervurs import db

excerpt_opts = {'before_match':'<i class="match">', 'after_match':'</i>', 'chunk_separator':' ... ', 'limit':400, 'around':15}

def http(req):
    q = req.args.get('q', [""])[0]
    
    db().execute("""
            INSERT INTO searchsuggestion 
                (id, suggestion, frequency)
            VALUES
                (0, %s, %s)
            ON DUPLICATE KEY UPDATE
                frequency = frequency + 1
        """, (q, 1))
    
    sphinx = SphinxClient()
    
    search = sphinx.Query(q)
    
    req.posts = []
    if search and len(search['matches']):
        search_ids = [match['id'] for match in search['matches']]
        
        post_filter = Post.filter(search_id__in=search_ids, limit=req.args.get('limit', [10])[0], offset=req.args.get('page', [0])[0])
        posts = post_filter.fetchall(count=True)
        
        docs = reduce(lambda acc, x: acc + x, [[post.title, post.body] for post in posts], [])
        docs = sphinx.BuildExcerpts(docs, "idx1", q, excerpt_opts)
        
        posts_by_search_id = {}
        for i, post in enumerate(posts):
            post.matched_title = docs[i*2]
            post.matched_body = docs[i*2+1]
            posts_by_search_id[post.search_id] = post
            
        req.posts = [posts_by_search_id[id] for id in search_ids]
        req.pagination = post_filter
    
    return None
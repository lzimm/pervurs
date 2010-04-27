import datetime
from cStringIO import StringIO

from pervurs.deps import PyRSS2Gen
from pervurs.includes.urls import links
from pervurs.models import Post

def http(req):
    posts = req.settings.ref.posts.filter(order_by="posted", order_dir="DESC").fetchall()
    
    rss = PyRSS2Gen.RSS2(
            title = req.settings.ref.name,
            link = req.settings.ref.host,
            description = req.settings.ref.name,
            lastBuildDate = datetime.datetime.now(),

            items = [PyRSS2Gen.RSSItem(
                        title = post.title,
                        link = links['post'](post),
                        description = post.span + post.body,
                        guid = PyRSS2Gen.Guid(links['post'](post)),
                        pubDate = post.posted
                        ) for post in posts])

    output = StringIO()
    rss.write_xml(output)
    
    req.output = output.getvalue()
    output.close()

    return None
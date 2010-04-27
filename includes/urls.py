from pervurs.settings import AWS_ATTACHMENT_BASE, ATTACHMENT_SIZES

links = {
    'feed': lambda site: "/feed",
    
    'post': lambda post: "/view/%s/%s/%s/%s/" % (post.posted.year, post.posted.month, post.posted.day, post.title.replace(' ', '_')),
    'post_edit' : lambda post: "/admin/edit/%s/" % (post.id),
    'post_delete' : lambda post: "/admin/delete/%s/" % (post.id),
    'post_new' : lambda : "/admin/new/",
    
    'attachment_hot': lambda post: "%s/%s-%s-%s.png" % (AWS_ATTACHMENT_BASE, post.id, ATTACHMENT_SIZES[0][0], ATTACHMENT_SIZES[0][1]),
    'attachment_index': lambda post: "%s/%s-%s-%s.png" % (AWS_ATTACHMENT_BASE, post.id, ATTACHMENT_SIZES[0][0], ATTACHMENT_SIZES[0][1]),
    'attachment_featured': lambda post: "%s/%s-%s-%s.png" % (AWS_ATTACHMENT_BASE, post.id, ATTACHMENT_SIZES[2][0], ATTACHMENT_SIZES[2][1]),
    'attachment_post': lambda post: "%s/%s-%s-%s.png" % (AWS_ATTACHMENT_BASE, post.id, ATTACHMENT_SIZES[3][0], ATTACHMENT_SIZES[3][1]),

    'paginate_less': lambda req: "%s?%s&page=%s" % (req.path, reduce(lambda acc, p: acc + "&%s=%s" % (p[0],p[1]), [(k, v[0]) for k, v in req.args.iteritems() if k.lower() != "page"], ""), req.pagination.offset - 1),
    'paginate_more': lambda req: "%s?%s&page=%s" % (req.path, reduce(lambda acc, p: acc + "&%s=%s" % (p[0],p[1]), [(k, v[0]) for k, v in req.args.iteritems() if k.lower() != "page"], ""), req.pagination.offset + 1)
}
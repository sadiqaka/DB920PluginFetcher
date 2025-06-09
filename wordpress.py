from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from config import WORDPRESS_SITES

def send_draft_to_wordpress(title, content, link, sites=WORDPRESS_SITES):
    for site in sites:
        client = Client(site["url"], site["username"], site["password"])
        post = WordPressPost()
        post.title = title
        post.content = f"{content}\n\nOriginal: {link}"
        post.post_status = 'draft'
        client.call(NewPost(post))

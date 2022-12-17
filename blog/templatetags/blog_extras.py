from django.contrib.auth.models import User
from django.template import Library
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

from blog.models import Post

register = Library()


@register.filter
def author_details(author: User, current_user: User):
    if not isinstance(author, User):
        return ""
    if author == current_user:
        return format_html("<strong>me</strong>")
    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = author.username
    if author.email:
        return format_html('<a href="mailto:{}">{}</a>', author.email, name)
    return mark_safe(escape(name))


@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
    return format_html("</div>")


@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)


@register.simple_tag
def endcol():
    return format_html("</div>")


@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts, "fuck": "dddd"}

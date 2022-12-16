from django.contrib.auth.models import User
from django.template import Library
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = Library()

@register.filter
def author_details(author:User, current_user:User):
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
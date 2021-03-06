__author__ = 'Muhammads'

from django import template
from datetime import date
from ..models import RefreshRate

register = template.Library()


@register.filter(name='get_due_date_string')
def get_due_date_string(value):
    delta = value - date.today()

    if delta.days == 0:
        return "Today!"
    elif delta.days < 1:
        return "%s %s ago!" % (abs(delta.days),
                               ("day" if abs(delta.days) == 1 else "days"))
    elif delta.days == 1:
        return "Tomorrow"
    elif delta.days > 1:
        return "In %s days" % delta.days


@register.filter(name='add_ex')
def add_ex(value, arg):
    """Adds the arg to the value."""
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        try:
            return str(value) + str(arg)
        except Exception:
            return ''


@register.filter(name='strip')
def strip(value, arg=' '):
    result = value
    try:
        for i in arg:
            result = str(value).strip(i)
    except (TypeError, ValueError):
        return result
    except Exception:
        return value
    finally:
        return result


@register.filter(name='suffix')
def suffix(value, arg):
    try:
        return str(value) + str(arg)
    except:
        return value


@register.filter(name='prefix')
def prefix(value, arg):
    try:
        return str(arg) + str(value)
    except:
        return value


@register.filter(name='generate_refresh')
def generate_refresh(value):
    rates = RefreshRate.objects.all()
    result = ""

    for rate in rates:
        rate_value = str(rate.rate_value)
        result += "<li><a class=\"refresh\" rate=\"" + rate_value + \
                  "\" id=\"refresh_" + rate_value + "\" href=\"" + "#" + "\">" + rate.name + "</a></li>"

    return result

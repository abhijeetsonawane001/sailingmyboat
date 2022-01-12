from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from admin.helper import superuser_only
from django.contrib.auth.decorators import login_required

from main.models import Booking

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None


@login_required()
@superuser_only
def bookings_pdf(request):
    bookings = Booking.objects.all()

    pdf = render_to_pdf('bookings/list.html', {'title': "THIS IS TITLE"})
    response = HttpResponse(pdf, content_type="application/pdf")

    filename = "Bookings.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response
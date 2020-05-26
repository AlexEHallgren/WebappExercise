from django.views.generic.base import RedirectView

class EmptyPathRedirectView(RedirectView):
  url = '/movies'
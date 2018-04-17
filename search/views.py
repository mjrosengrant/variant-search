"""Views required to enable search."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index_view(request):
    """Render the main search page."""
    return render(request, 'search/index.html', {})

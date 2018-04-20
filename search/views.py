"""Views required to enable search."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render
from django.urls import reverse

from api.models import Variant


def index_view(request):
    """Render the main search page."""
    genes_list = [v.gene for v in Variant.objects.all()]
    genes_set = set(genes_list)
    context = {
        'api_url': reverse('api:variants'),
        'gene_choices': json.dumps(list(genes_set))
    }
    return render(request, 'search/index.html', context)

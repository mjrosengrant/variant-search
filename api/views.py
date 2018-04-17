# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse

from api.models import Variant


def variant_list_view(request):
	"""List all variants in system."""
	queryset = Variant.objects.exclude(gene="")
	if 'query' in request.GET:
		queryset = queryset.filter(gene=request.GET['query'])
	data = [{'gene': v.gene, 'id': v.pk} for v in queryset[:100]]
	return HttpResponse(json.dumps(data))

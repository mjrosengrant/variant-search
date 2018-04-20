# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse

from api.models import Variant


def variant_list_view(request):
	"""List all variants in system.

	Provides option to filter by gene name using GET param `query`.
	"""
	queryset = Variant.objects.exclude(gene="")
	if 'query' in request.GET and request.GET['query']:
		queryset = queryset.filter(gene=request.GET['query'])

	data = [
		{
			'gene': v.gene,
			'nucleotide_change': v.nucleotide_change,
			'protein_change': v.protein_change,
			'alias': v.alias,
			'region': v.region,
			'reported_classification': v.reported_classification,
			'last_evaluated': v.last_evaluated.isoformat() if v.last_evaluated else None,
			'last_updated': v.last_updated.isoformat() if v.last_updated else None,
		} for v in queryset
	]
	return HttpResponse(json.dumps(data))

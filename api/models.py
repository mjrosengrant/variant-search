# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Variant(models.Model):
	"""Variants of Genes."""

	headers = [
		'Gene',
		'Nucleotide Change',
		'Protein Change',
		'Other Mappings',
		'Alias',
		'Transcripts',
		'Region',
		'Reported Classification',
		'Inferred Classification',
		'Source',
		'Last Evaluated',
		'Last Updated',
		'URL',
		'Submitter Comment',
		'Assembly',
		'Chr',
		'Genomic Start',
		'Genomic Stop',
		'Ref',
		'Alt',
		'Accession',
		'Reported Ref',
		'Reported Alt'
	]
	gene = models.CharField(max_length=16, blank=True)

	def __unicode__(self):
		"""String representation of object."""
		return "%s - %d" % (self.gene, self.pk)

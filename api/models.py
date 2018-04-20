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
    nucleotide_change = models.CharField(max_length=128, blank=True)
    protein_change = models.CharField(max_length=128, blank=True)
    alias = models.CharField(max_length=128, blank=True)
    region = models.CharField(max_length=128, blank=True)
    reported_classification = models.CharField(max_length=128, blank=True)
    last_evaluated = models.DateField(null=True, blank=True)
    last_updated = models.DateField(null=True, blank=True)

    def __unicode__(self):
        """String representation of object."""
        return "%s - %d" % (self.gene, self.pk)

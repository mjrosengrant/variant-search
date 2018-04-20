"""Management command to import symptom and conditions data."""
import csv

from django.core.management.base import BaseCommand

from api.models import Variant


class Command(BaseCommand):
	"""Management command to import data from symptoms.csv."""

	help = 'Import provided variant information into database.'

	def handle(self, *args, **options):
		"""Execute command."""
		with open('variant_results.tsv', 'rb') as tsvin:
			tsvin = csv.reader(tsvin, delimiter='\t')
			count = 0
			for row in tsvin:
				gene_name = row[0]
				nucleotide_change = row[1]
				protein_change = row[2]
				alias = row[4]
				region = row[6]
				reported_classification = row[7]
				last_evaluated = row[10] if row[10] != '' else None
				last_updated = row[11] if row[11] != '' else None

				if not gene_name or gene_name == 'Gene':
					continue

				Variant.objects.create(
					gene=gene_name,
					nucleotide_change=nucleotide_change,
					protein_change=protein_change,
					alias=alias,
					region=region,
					reported_classification=reported_classification,
					last_evaluated=last_evaluated,
					last_updated=last_updated,
				)
				print gene_name
			print '%d Variants created' % count

"""Management command to import symptom and conditions data."""
import csv

from django.core.management.base import BaseCommand

from api.models import Variant


class Command(BaseCommand):
    """Management command to import data from symptoms.csv."""

    help = 'Import provided variant information into database.'

    def handle(self, *args, **options):
        """Execute command."""
        with open('api/variant_results.tsv', 'rb') as tsvin:
            tsvin = csv.reader(tsvin, delimiter='\t')
            count = 0
            for row in tsvin:
                gene_name = row[0]
                if gene_name == 'Gene':
                    # Skip row with column names
                    continue

                Variant.objects.create(gene=gene_name)
                count += 1
                print gene_name
            print '%d Variants created' % count

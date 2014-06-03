from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from entitlements import models

class Command(BaseCommand):
    help = "Initializes the database fixtures and puts sample data into ElasticSearch"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        models.create_initial_db()
        models.create_initial_es()



from django.core.management.base import BaseCommand, CommandError

from elasticsearch_dsl import connections

from catalog.constants import ES_INDEX, ES_MAPPING


class Command(BaseCommand):
    from elasticsearch_dsl import Index

    def handle(self, *args, **kwargs):
        self.stdout.write(f'deleting "{ES_INDEX}" index...')
        from elasticsearch import Elasticsearch
        connection = connections.get_connection()

        connection.indices.delete(index='wine', ignore=[400, 404])
        self.stdout.write(
            f'deleted   "{ES_INDEX}" successfully')

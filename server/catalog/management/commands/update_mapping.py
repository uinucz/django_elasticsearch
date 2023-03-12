from django.core.management.base import BaseCommand, CommandError

from elasticsearch_dsl import connections

from catalog.constants import ES_INDEX, ES_MAPPING


class Command(BaseCommand):
    help = 'Updates a mapping on an Elasticsearch index'

    def handle(self, *args, **kwargs):
        index = 'wine'

        self.stdout.write(f'updating mapping on "{index}" index...')
        connection = connections.get_connection()

        if connection.indices.exists(index=ES_INDEX):
            connection.indices.put_mapping(index=ES_INDEX, body=ES_MAPPING)
            self.stdout.write(f'updated mapping on "{index}" successfully')
        else:
            raise CommandError(f'Index "{index}" does not exist')

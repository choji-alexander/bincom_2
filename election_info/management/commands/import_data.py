from django.core.management.base import BaseCommand
import json
import sqlite3


class Command(BaseCommand):
    help = 'Process JSON data'

    #def add_arguments(self, parser):
        #parser.add_argument('data.json', type=str, help='/election_info/static/data.json')

    def handle(self, *args, **options):
        json_file = 'election_info/static/data.json'

        # Read the JSON file
        with open(json_file, 'r') as file:
            json_data = json.load(file)

        # Process the JSON data
        # Perform actions or tasks based on the JSON data
        #for item in json_data:

            # Process each item in the JSON data as needed
            #self.stdout.write(f"Processing item: {item}")
            #for each in item:
                #self.stdout.write(f"Processing item: {each}")

        self.stdout.write("JSON data processing complete.")


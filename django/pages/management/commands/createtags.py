from django.core.management.base import BaseCommand, CommandError

from pages.models import Tag

FRENCH_TAGS = """Santé
Alimentaire
Education
Télétravail
Sécurité et droit
Transport
Tourisme
Informatique et Multimédia
Sport
Musique
Cinéma
Voyage
Culture
Cuisine
Nature & Environnement
Psychologie
Positivité
Motivation
Humour
Récits
Arts
""".splitlines()


class Command(BaseCommand):
    help = "Creates a set of predefined hashtags"

    def handle(self, *args, **options):
        self.stdout.write("creatings tags:\n")

        for t in FRENCH_TAGS:
            self.stdout.write("- " + t)

        for t in FRENCH_TAGS:
            Tag.objects.create(name=t.lower())

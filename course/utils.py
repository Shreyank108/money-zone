from django.utils.text import slugify
import uuid


def generate_slug(name: str) -> str:
    from .models import Package
    name = slugify(name)

    while Package.objects.filter(slug=name).exists():
        name = slugify(name) + '-' + str(uuid.uuid4())[:4]

    return name

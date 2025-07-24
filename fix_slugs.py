from app.models import Project
from django.utils.text import slugify

def run():
    projects = Project.objects.all()
    for project in projects:
        if not project.slug:
            base_slug = slugify(project.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exclude(id=project.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            project.slug = slug
            project.save()
    print("Done fixing slugs")

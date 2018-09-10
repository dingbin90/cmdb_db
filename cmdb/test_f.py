import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb_db.settings")
    import django
    django.setup()

    from cmdb import models

    obj = models.Asset.objects.all().values("")
    print(obj)




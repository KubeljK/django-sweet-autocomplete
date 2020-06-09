from django.conf import settings

settings.SWEETAUTOCOMPLETE = getattr(
    settings, "SWEETAUTOCOMPLETE",
    {
        "enable_unique": False  # SQLite doesn't support it.
    }
)

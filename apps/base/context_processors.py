from django.conf import settings

from template_utils.context_processors import settings_processor

base_settings = settings_processor(
    'MAPS_API_KEY','MEDIA_URL'
)
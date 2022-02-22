import uuid
from pathlib import Path

import requests
from celery import shared_task
from django.conf import settings

CAT_URL = 'https://thiscatdoesnotexist.com'


@shared_task
def download_cat():
    r = requests.get(CAT_URL)
    file_ext = r.headers.get('Content-Type').split('/')[1]
    with Path(settings.BASE_DIR / 'cats' / f'{uuid.uuid4()}.{file_ext}').open('wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)


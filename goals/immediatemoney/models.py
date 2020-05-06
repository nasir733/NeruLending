from django.db import models
from django.utils.safestring import mark_safe
from user.models import Profile
import uuid
import os

app_name = 'repairbusinesscredit'


def get_file_path(instance, filename):
    return os.path.join(f'documents/{uuid.uuid4()}', filename)

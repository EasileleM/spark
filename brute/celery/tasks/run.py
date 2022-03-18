from .worker import bruteForcePass
from .const import ALLOWED_PASSWORD_CHARACTERS

for char in ALLOWED_PASSWORD_CHARACTERS:
    bruteForcePass.apply_async([char], queue='workerTasksQ')

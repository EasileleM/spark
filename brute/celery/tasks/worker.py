import itertools
from .encriptFile import password_decrypt
from .const import ALLOWED_PASSWORD_CHARACTERS, SECRET
from base64 import urlsafe_b64decode as b64d
from celery.contrib.abortable import AbortableTask
from .celery import app
from .master import handleResult

@app.task(bind=True, base=AbortableTask)
def bruteForcePass(self, firstPassChar):
    with open("secret.txt", "rb") as file:
        enryptedSecret = b64d(file.read())

        def tryPass(resultPass):
            try:
                return password_decrypt(enryptedSecret, resultPass).decode() == SECRET
            except:
                return False

        if tryPass(firstPassChar):
            return firstPassChar

        for restPassLen in range(1, 20):
            def generatePass(chars):
                yield from itertools.product(chars, repeat=restPassLen)

            for generatedPass in generatePass(ALLOWED_PASSWORD_CHARACTERS):
                if self.is_aborted():
                    return None
                resultPass = firstPassChar + ''.join(generatedPass)
                print('Trying %s' % resultPass)

                if tryPass(resultPass):
                    handleResult.apply_async([resultPass], queue='masterTasksQ')
                    return resultPass
    return None

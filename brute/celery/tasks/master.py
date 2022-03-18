from .celery import app
#from celery.contrib.abortable import AbortableAsyncResult

@app.task(bind=True)
def handleResult(self, result):
    with open("result.txt", "w") as file:
        file.write(result)

    workersData = app.control.inspect().active()

    app.control.purge()

    for workerId in workersData.keys():
        for task in workersData[workerId]:
            if self.request.id != task['id']:
                #AbortableAsyncResult(task['id']).abort()
                app.control.revoke(task['id'], terminate=True)

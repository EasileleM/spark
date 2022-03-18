from celery import Celery

app = Celery('tasks',
    broker='pyamqp://user:user@rabbitmq//',
    backend='rpc://',
    include=['tasks.master', 'tasks.worker']
)

app.conf.update(
    task_routes = {
        'tasks.master.handleResult': {'queue': 'masterTasksQ'},
        'tasks.worker.bruteForcePass': {'queue': 'workerTasksQ'},
    },
)

if __name__ == '__main__':
    app.start()

from app.app import celery_app
from app.models.model import Order
from app.services.order_service import get_db
@celery_app.task
def process_order_task(data):
    db = get_db()
    order_id = data['order_id']
    # add business logic here
    print(f'Task completed with data: {data}')
    return {'result': 'Task finished!'}
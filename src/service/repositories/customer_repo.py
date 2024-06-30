from .repository import BaseRepository
from src.models.customer import Customer

class CustomerRepo(BaseRepository):

    def __init__(self, model=Customer):
        super().__init__(model)

    async def get_by_id(self, id: int):
        return self.db.query(Customer).filter(Customer.customer_id == id).first()
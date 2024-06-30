from abc import ABC
from src.dbs.postgres import get_db, Base


class BaseRepository(ABC):

    def __init__(self, model: Base):
        self.db = next(get_db())
        self.model = model

    async def get_by_id(self, id: int):
        raise NotImplementedError

from abc import ABC
from .repositories.repository import BaseRepository


class BaseService(ABC):

    def __init__(self, repository: BaseRepository):
        self.__repo = repository

    async def get_by_id(self, id: int):
        return await self.__repo.get_by_id(id)
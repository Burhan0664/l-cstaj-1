from typing import List

from .models import Case


class CaseService:
    """
    Davalar için CRUD Servisi
    """
    def __init__(self):
        pass

    async def gets(self) -> List[Case]:
        """
        Tüm dava verilerini çeker
        :return: List[Case]
        """
        pass

    async def get(self, case_id: int) -> Case:
        """
        ID'si verilen dava verisini çeker
        :param case_id:
        :return:
        """
        pass

    async def post(self, case: Case):
        """
        Dava oluşturur.
        :param case:
        :return:
        """
        pass

    async def put(self, case_id: int, data: Case) -> Case:
        """
        ID'si verilen davayı günceller
        :param case_id:
        :param data:
        :return:
        """
        pass

    async def delete(self, case_id) -> int:
        """
        ID'si verilen davayı siler
        :param case_id:
        :return:
        """
        pass
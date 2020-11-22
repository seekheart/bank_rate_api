import pymongo
import config
from loguru import logger


class MongoEngine:
    def __init__(self, collection: str) -> None:
        """Constructor for mongodb connection
        Args:
            collection: name of collection to operate on.
        """

        self._host = config.MONGO_HOST
        self._port = config.MONGO_PORT
        self._db_name = config.MONGO_DB_NAME
        self._collection = collection

        try:
            self.db = pymongo.MongoClient(self._host, self._port)[self._db_name]
            self.db = self.db.get_collection(self._collection)
        except ConnectionError:
            logger.error(f'Error connecting to database! host = {self._host} port = {self._port} db name = {self._db_name}')

    def find_all(self) -> list:
        pass

    def save_one(self, data: dict) -> bool:
        pass

    def save_all(self, data: list) -> bool:
        pass



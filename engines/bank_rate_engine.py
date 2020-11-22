from .mongo_engine import MongoEngine
import pymongo
from loguru import logger

class BankRateEngine(MongoEngine):
    def __init__(self):
        super(BankRateEngine, self).__init__('bank_rates')

    def find_all(self) -> list:
        return [doc for doc in self.db.find().sort('_id', pymongo.ASCENDING)]

    def drop_and_replace_data(self, new_data: list) -> bool:
        logger.info('Deleting old bank rates')
        try:
            self.db.delete_many(filter={})
        except Exception as e:
            logger.error(e)
            return False

        logger.info('Successfully deleted old data, adding new data')
        self.db.insert_many(new_data)
        return True


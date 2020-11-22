from .mongo_engine import MongoEngine
from loguru import logger
from uuid import uuid4

class BankRateEngine(MongoEngine):
    def __init__(self):
        super(BankRateEngine, self).__init__('bank_rates')

    def find_all(self) -> list:
        return [doc for doc in self.db.find()]

    def drop_and_replace_data(self, new_data: list) -> bool:
        logger.info('Deleting old bank rates')
        try:
            self.db.delete_many(filter={})
        except Exception as e:
            logger.error(e)
            return False

        logger.info('Successfully deleted old data, adding new data')
        cleaned_data = []
        for doc in new_data:
            doc['_id'] = uuid4()
            cleaned_data.append(doc)
        self.db.insert_many(cleaned_data)
        return True


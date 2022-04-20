from database import Database


database = Database()

class Item:
    def __init__(self, name, attribute=None, value=0):
        self.name = name
        self.attribute = attribute
        self.value = value

    @classmethod
    def get_all(cls):
        item_dicts = database.get_all_champion("Select * from items")
        items = [Item(
        name=item_dicts.get('name'),
        attribute=item_dicts.get('attribute'),
        value=item_dicts.get('value')
        ) for item_dicts in item_dicts]
        return [item for item in items]
    
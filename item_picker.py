from item import Item
from picker import RecordPicker


class ItemPicker(RecordPicker):
    def __init__(self):
        self.selected_record = None
        super().__init__('item', Item.get_all())

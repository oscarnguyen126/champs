from champion import Champion
from picker import RecordPicker


class ChampionPicker(RecordPicker):
    def __init__(self):
        self.selected_record = None
        super().__init__('champion', Champion.get_all())

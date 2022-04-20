class RecordPicker:
    def __init__(self, record_type, records):
        self.selected_record = None
        self.record_type = record_type
        self.records = records

    def pick_record(self):
        print(f"Choose a {self.record_type}: ")
        available_records = self.records
        if self.selected_record:
            available_records = [
                record for record in self.records if record.name != self.selected_record.name]
        self.print_record_list(available_records)

        input_idx = input()
        record = available_records[int(input_idx) - 1]
        self.selected_record = record
        print(f'{record.name} has been selected!')
        return record

    def print_record_list(self, records):
        for idx, record in enumerate(records):
            print(f'{idx + 1}: {record.name}')

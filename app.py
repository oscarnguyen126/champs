from champion_picker import ChampionPicker
from item_picker import ItemPicker
from database import Database

champion_picker = ChampionPicker()
item_picker = ItemPicker()
database = Database()


input_champ_1st = champion_picker.pick_record()
input_champ_1st.add_item(
    item_picker.pick_record()
)
input_champ_2nd = champion_picker.pick_record()
input_champ_2nd.add_item(
    item_picker.pick_record()
)

if input_champ_1st.name == input_champ_2nd.name:
    print("Violate rules")
else:
    while input_champ_1st.hp > 0 and input_champ_2nd.hp > 0:
        champ_atk_1st = None
        champ_atk_2nd = None
        champ_with_greater_atk_speed = input_champ_1st if input_champ_1st.atk_speed > input_champ_2nd.atk_speed else input_champ_2nd
        champ_with_lower_atk_speed = input_champ_1st if input_champ_1st.atk_speed <= input_champ_2nd.atk_speed else input_champ_2nd
        additional_attack = round(
            champ_with_greater_atk_speed.atk_speed / champ_with_lower_atk_speed.atk_speed) - 1

        if input_champ_1st.range > input_champ_2nd.range:
            champ_atk_1st = input_champ_1st
            champ_atk_2nd = input_champ_2nd
        elif input_champ_1st.range < input_champ_2nd.range:
            champ_atk_1st = input_champ_2nd
            champ_atk_2nd = input_champ_1st
        else:
            champ_atk_1st = champ_with_greater_atk_speed
            champ_atk_2nd = champ_with_lower_atk_speed

        champ_atk_1st.normal_attack(champ_atk_2nd)
        champ_atk_2nd.normal_attack(champ_atk_1st)

        for i in range(additional_attack):
            champ_with_greater_atk_speed.normal_attack(
                champ_with_lower_atk_speed)

    print(input_champ_2nd.name if input_champ_1st.hp <=
          0 else input_champ_1st.name)

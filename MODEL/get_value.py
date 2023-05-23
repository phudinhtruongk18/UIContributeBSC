import json

def get_setting_value():
    with open("./DATA/setting.json", "r") as jsonfile:
        sheet_nek = json.load(jsonfile)

    def get_or_nomal(truong, mac_dinh):
        try:
            value = sheet_nek[truong]
        except Exception as e:
            print(e)
            value = mac_dinh
        return value

    timer = get_or_nomal(truong="timer", mac_dinh='')
    return timer
    
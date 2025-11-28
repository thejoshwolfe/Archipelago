#!/usr/bin/env python3
import zlib
import collections
import re

from Utils import restricted_loads

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-save", metavar="AP_*.apsave", required=True)
    parser.add_argument("--from-multidata", metavar="AP_*.archipelago", required=True)
    parser.add_argument("--from-spoiler", metavar="AP_*_Spoiler.txt", required=True)
    args = parser.parse_args()

    with open(args.from_multidata, "rb") as f:
        data = f.read()
        assert data[0] == 3
        multidata = restricted_loads(zlib.decompress(data[1:]))
    slot_id_to_name = {
        int(slot_id_str): slot.name
        for slot_id_str, slot in multidata["slot_info"].items()
    }
    slot_id_to_datapackage = {
        int(slot_id_str): multidata["datapackage"][slot.game]
        for slot_id_str, slot in multidata["slot_info"].items()
    }
    game_to_location_id_to_name = {
        game_name: { id: name for name, id in datapackage["location_name_to_id"].items() }
        for game_name, datapackage in multidata["datapackage"].items()
    }
    game_to_item_id_to_name = {
        game_name: { id: name for name, id in datapackage["item_name_to_id"].items() }
        for game_name, datapackage in multidata["datapackage"].items()
    }
    slot_id_to_location_id_to_name = {
        int(slot_id_str): game_to_location_id_to_name[slot.game]
        for slot_id_str, slot in multidata["slot_info"].items()
    }
    slot_id_to_item_id_to_name = {
        int(slot_id_str): game_to_item_id_to_name[slot.game]
        for slot_id_str, slot in multidata["slot_info"].items()
    }

    with open(args.from_save, "rb") as f:
        save_data = restricted_loads(zlib.decompress(f.read()))

    with open(args.from_spoiler, "r") as f:
        spoiler_spheres = parse_spoiler(f.read(), slot_id_to_datapackage)

    slot_id_to_checked_locations = {}
    for (team_id, slot_id), checked_locations in save_data["location_checks"].items():
        assert team_id == 0, "Team support is only partially implemented."
        slot_id_to_checked_locations[slot_id] = checked_locations

    for spoiler_sphere in spoiler_spheres:
        print("sphere:")
        for location_slot_id, location_id, item_slot_id, item_id in spoiler_sphere:
            is_gotten = location_id in slot_id_to_checked_locations[location_slot_id]
            print("- [{}] `{}` checks `{}`, sends `{}` to `{}`".format(
                ("x" if is_gotten else " "),
                slot_id_to_name[location_slot_id],
                slot_id_to_location_id_to_name[location_slot_id][location_id],
                slot_id_to_item_id_to_name[item_slot_id][item_id],
                slot_id_to_name[item_slot_id],
            ))

    # Done

def parse_spoiler(contents, slot_id_to_datapackage):
    # Find slots, player names, and game names.
    [player_count_str] = re.findall(r'^Players: +(\d+)$', contents, re.MULTILINE) # An error here means this doesn't look like a spoiler log.
    is_multiplayer = player_count_str != "1"
    if is_multiplayer:
        slot_name_to_id = {}
        for slot_id_str, slot_name in re.findall(r'^Player (\d+): (.*)$', contents, re.MULTILINE):
            slot_id = int(slot_id_str)
            slot_name_to_id[slot_name] = slot_id
        if len(slot_name_to_id) == 0: raise Exception("doesn't look like a spoiler log")

    match = re.search(r'^Playthrough:$', contents, re.MULTILINE)
    if match == None: raise Exception("spoiler does not contain a playthrough")
    contents = contents[match.span()[1]:]

    spoiler_spheres = [
        # (location_slot_id, location_id, item_slot_id, item_id),
        # (1, 123456789, 3, 23456789),
    ]
    # Example:
    #   0: {
    #     Dashmaster (player_1)
    #   }
    #   1: {
    #     Bow Weapon Unlock Location (player_3): progressive-processing (player_4)
    # ...
    for sphere_paragraph in re.findall(r'^\d+: \{$(.*?)^\}$', contents, re.MULTILINE | re.DOTALL):
        spoiler_sphere = []
        for line in sphere_paragraph.splitlines():
            try:
                location_str, item_str = line.split(":", 1)
            except ValueError:
                continue # skip sphere 0 starter items.
            # Multiplayer has different syntax.
            if is_multiplayer:
                # Location Name (slot_name): Item Name (slot_name)
                location_name, location_slot_name = re.match(r'^  (.*) \((.*)\)$', location_str).groups()
                item_name, item_slot_name = re.match(r'^ (.*) \((.*)\)$', item_str).groups()
                # Reverse lookup names back to ids
                location_slot_id = slot_name_to_id[location_slot_name]
                item_slot_id = slot_name_to_id[item_slot_name]
            else:
                # Location Name: Item Name
                location_name = location_str
                item_name = item_str
                location_slot_id = item_slot_id = 1
            try:
                location_id = slot_id_to_datapackage[location_slot_id]["location_name_to_id"][location_name]
            except KeyError:
                if location_slot_id == item_slot_id:
                    continue # "events" trigger this, such as defeating a boss locally.
                raise
            item_id = slot_id_to_datapackage[item_slot_id]["item_name_to_id"][item_name]

            spoiler_sphere.append((location_slot_id, location_id, item_slot_id, item_id))

        if spoiler_sphere:
            spoiler_spheres.append(spoiler_sphere)
    return spoiler_spheres

if __name__ == "__main__":
    main()

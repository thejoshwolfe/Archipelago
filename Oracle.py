#!/usr/bin/env python3
import zlib
import collections

from Utils import restricted_loads

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-save", metavar="AP_*.apsave", required=True)
    parser.add_argument("--from-multidata", metavar="AP_*.archipelago", required=True)
    args = parser.parse_args()

    with open(args.from_multidata, "rb") as f:
        data = f.read()
        assert data[0] == 3
        multidata = restricted_loads(zlib.decompress(data[1:]))

    with open(args.from_save, "rb") as f:
        save_data = restricted_loads(zlib.decompress(f.read()))


    slot_id_to_checked_locations = {}
    for (team_id, slot_id), checked_locations in save_data["location_checks"].items():
        assert team_id == 0, "Team support is only partially implemented."
        slot_id_to_checked_locations[slot_id] = checked_locations
    slot_id_to_location_id_to_location_tuple = multidata["locations"]

    spheres = multidata["spheres"]
    todo_list = collections.defaultdict(list)
    for sphere in spheres:
        for slot_id, location_ids in sphere.items():
            remaining_location_ids = location_ids - slot_id_to_checked_locations[slot_id]
            for location_id in remaining_location_ids:
                # Only count advancement items.
                item_id, receiver_slot_id, flags = slot_id_to_location_id_to_location_tuple[slot_id][location_id]
                if flags & 0b001 and not item_id in ignore_item_ids:
                    todo_list[slot_id].append(location_id)
        if todo_list: break

    print("")

ignore_item_ids = {
    16777320, # Hollow Knight - Racid Egg
    16777352, # Hollow Knight - Grub
}

if __name__ == "__main__":
    main()

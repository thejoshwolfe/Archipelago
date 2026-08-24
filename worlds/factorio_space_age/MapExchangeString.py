# This is based on the work in: https://github.com/rfvgyhn/factorio-exchange-string-parser
# (with https://github.com/rfvgyhn/factorio-exchange-string-parser/pull/7 )

supported_versions = {
    (2, 1, 14, 1),
    (2, 1, 15, 2),
}

import base64, struct, zlib
from io import BytesIO

def parse_map_exchange_string(s):
    s = s.strip()
    if (s[:3], s[-3:]) != (">>>", "<<<"):
        raise ValueError("Invalid map exchange string format. It's supposed to be wrapped in >>>these<<< things. got: " + repr(s))
    b = zlib.decompress(base64.b64decode(s[3:-3]))
    f = BytesIO(b)
    version = struct.unpack("<HHHH", f.read(8))
    if version not in supported_versions:
        raise NotImplementedError(f"Map exchange string was generated with Factorio version {'.'.join(str(x) for x in version)}. The only supported versions are: {', '.join('.'.join(str(x) for x in v) for v in sorted(supported_versions))} is supported.")

    _unknown = f.read(1)

    value = read_map_exchange_settings(f)

    checksum = read_uint32(f)
    if len(f.read(1)) > 0:
        raise ValueError("Expected EOF")
    if zlib.crc32(b[:-4]) != checksum:
        raise ValueError("Checksum failed")

    return value

def format_map_exchange_string(value):
    f = BytesIO()
    f.write(struct.pack("<HHHH", *sorted(supported_versions)[0]))
    f.write(b"\x00") # _unknown

    write_map_exchange_settings(f, value)

    write_uint32(f, zlib.crc32(f.getvalue())) # checksum

    s = ">>>" + base64.b64encode(zlib.compress(f.getvalue())).decode("utf8") + "<<<"
    return s


#################
# General types #
#################

def read_bool (f): return bool(f.read(1)[0])
def write_bool(f, value): f.write(b"\x01" if value else b"\x00")
Bool = (read_bool, write_bool)

def read_uint16  (f): return struct.unpack("<H", f.read(2))[0]
def read_int16   (f): return struct.unpack("<h", f.read(2))[0]
def read_uint32  (f): return struct.unpack("<L", f.read(4))[0]
def read_int32   (f): return struct.unpack("<l", f.read(4))[0]
def read_float32 (f): return struct.unpack("<f", f.read(4))[0]
def read_float64 (f): return struct.unpack("<d", f.read(8))[0]
def write_uint16 (f, value): f.write(struct.pack("<H", value))
def write_int16  (f, value): f.write(struct.pack("<h", value))
def write_uint32 (f, value): f.write(struct.pack("<L", value))
def write_int32  (f, value): f.write(struct.pack("<l", value))
def write_float32(f, value): f.write(struct.pack("<f", value))
def write_float64(f, value): f.write(struct.pack("<d", value))
Uint16  = (read_uint16,  write_uint16)
Int16   = (read_int16,   write_int16)
Uint32  = (read_uint32,  write_uint32)
Int32   = (read_int32,   write_int32)
Float32 = (read_float32, write_float32)
Float64 = (read_float64, write_float64)

def read_uint_8_or_32(f):
    value = f.read(1)[0]
    if value == 0xff:
        value = read_uint32(f)
    return value
def write_uint_8_or_32(f, value):
    if value < 0xff:
        f.write(bytes([value]))
    else:
        f.write(bytes([0xff]))
        write_uint32(f, value)

def read_str(f):
    l = read_uint_8_or_32(f)
    return f.read(l).decode("utf8")
def write_str(f, value):
    write_uint_8_or_32(f, len(value))
    f.write(value.encode("utf8"))
Str = (read_str, write_str)

def Optional(Child):
    read_child, write_child = Child
    def read(f):
        if not read_bool(f):
            return None
        return read_child(f)
    def write(f, value):
        if value is None:
            write_bool(f, False)
        else:
            write_bool(f, True)
            write_child(f, value)
    return (read, write)

def Array(Child):
    read_child, write_child = Child
    def read(f):
        l = read_uint_8_or_32(f)
        value = [read_child(f) for _ in range(l)]
        return value
    def write(f, value):
        write_uint_8_or_32(f, len(value))
        for x in value:
            write_child(f, x)
    return (read, write)

def Dict(Child):
    read_child, write_child = Child
    def read(f):
        l = read_uint_8_or_32(f)
        value = {read_str(f): read_child(f) for _ in range(l)}
        return value
    def write(f, value):
        write_uint_8_or_32(f, len(value))
        for k, v in value.items():
            write_str(f, k)
            write_child(f, v)
    return (read, write)

class AssertAllKeysUsed:
    """ Wraps a dict, and on exit asserts that every key has been read. """
    def __init__(self, d):
        assert type(d) == dict, repr(d)
        self.d = d
        self.keys_left = set(d.keys())
    def __enter__(self): return self
    def __exit__(self, *args):
        if self.keys_left:
            raise KeyError("unrecognized keys: " + ", ".join(json.dumps(k) for k in self.keys_left))
    def __contains__(self, k):
        return k in self.d
    def __getitem__(self, k):
        self.keys_left.discard(k)
        return self.d[k]
    def get(self, k, default=None):
        self.keys_left.discard(k)
        return self.d.get(k, default)

def Struct(fields):
    def read(f):
        value = {
            field_name: read_field(f)
            for field_name, (read_field, write_field) in fields.items()
        }
        return value
    def write(f, value):
        with AssertAllKeysUsed(value) as value:
            for field_name, (read_field, write_field) in fields.items():
                write_field(f, value[field_name])
    return (read, write)


##################
# Factorio stuff #
##################

# https://lua-api.factorio.com/latest/types/FrequencySizeRichness.html
FrequencySizeRichness = Struct({
    "frequency": Float32,
    "size": Float32,
    "richness": Float32,
})

# https://lua-api.factorio.com/latest/types/AutoplaceSettings.html
AutoplaceSettings = Struct({
    "treat_missing_as_default": Bool,
    "settings": Dict(FrequencySizeRichness),
})

# https://lua-api.factorio.com/latest/types/MapPosition.html
read_xy, write_xy = Struct({
    "x": Int32,
    "y": Int32,
})
def read_map_position(f):
    x_diff = read_int16(f)
    if x_diff != 0x7fff:
        raise ValueError("Expected MapPosition to always be in 32 bit format")
    return read_xy(f)
def write_map_position(f, value):
    write_int16(f, 0x7fff) # x_diff
    write_xy(f, value)
MapPosition = (read_map_position, write_map_position)

# https://lua-api.factorio.com/latest/types/BoundingBox.html
BoundingBox = Struct({
    "left_top": MapPosition,
    "right_bottom": MapPosition,
    "orientation": Struct({
        "x": Int16,
        "y": Int16,
    }),
})

# https://lua-api.factorio.com/latest/types/CliffPlacementSettings.html
CliffPlacementSettings = Struct({
    "name": Str,
    "control": Str,
    "cliff_elevation_0": Float32,
    "cliff_elevation_interval": Float32,
    "richness": Float32,
    "cliff_smoothing": Float32,
})

# https://lua-api.factorio.com/latest/types/TerritorySettings.html
TerritorySettings = Struct({
    "units": Array(Str),
    "territory_index_expression": Str,
    "territory_variation_expression": Str,
    "minimum_territory_size": Uint32,
})

# https://lua-api.factorio.com/latest/types/MapGenSettings.html
MapGenSettings = Struct({
    "autoplace_controls": Dict(FrequencySizeRichness),
    "autoplace_settings": Dict(AutoplaceSettings),
    "default_enable_all_autoplace_controls": Bool,
    "seed": Uint32,
    "width": Uint32,
    "height": Uint32,
    "area_to_generate_at_start": BoundingBox,
    "starting_area": Float32,
    "peaceful_mode": Bool,
    "no_enemies_mode": Bool,
    "starting_points": Array(MapPosition),
    "property_expression_names": Dict(Str),
    "cliff_settings": CliffPlacementSettings,
    "territory_settings": Optional(TerritorySettings),
})

# https://lua-api.factorio.com/latest/types/PollutionSettings.html
PollutionSettings = Struct({
    "enabled": Optional(Bool),
    "diffusion_ratio": Optional(Float64),
    "min_to_diffuse": Optional(Float64),
    "ageing": Optional(Float64),
    "expected_max_per_chunk": Optional(Float64),
    "min_to_show_per_chunk": Optional(Float64),
    "min_pollution_to_damage_trees": Optional(Float64),
    "pollution_with_max_forest_damage": Optional(Float64),
    "pollution_per_tree_damage": Optional(Float64),
    "pollution_restored_per_tree_damage": Optional(Float64),
    "max_pollution_to_restore_trees": Optional(Float64),
    "enemy_attack_pollution_consumption_modifier": Optional(Float64),
})

# https://lua-api.factorio.com/latest/types/EnemyEvolutionSettings.html
EnemyEvolutionSettings = Struct({
    "enabled": Optional(Bool),
    "time_factor": Optional(Float64),
    "destroy_factor": Optional(Float64),
    "pollution_factor": Optional(Float64),
})

# https://lua-api.factorio.com/latest/types/EnemyExpansionSettings.html
EnemyExpansionSettings = Struct({
    "enabled": Optional(Bool),
    "max_expansion_distance": Optional(Uint32),
    "min_expansion_distance": Optional(Uint32),
    "friendly_base_influence_radius": Optional(Uint32),
    "enemy_building_influence_radius": Optional(Uint32),
    "building_coefficient": Optional(Float64),
    "other_base_coefficient": Optional(Float64),
    "neighbouring_chunk_coefficient": Optional(Float64),
    "neighbouring_base_chunk_coefficient": Optional(Float64),
    "max_colliding_tiles_coefficient": Optional(Float64),
    "settler_group_min_size": Optional(Uint32),
    "settler_group_max_size": Optional(Uint32),
    "evolution_group_size_factor": Optional(Float64),
    "min_expansion_cooldown": Optional(Uint32),
    "max_expansion_cooldown": Optional(Uint32),
})

# https"://lua-api.factorio.com/latest/types/UnitGroupSettings.html
UnitGroupSettings = Struct({
    "min_group_gathering_time": Optional(Uint32),
    "max_group_gathering_time": Optional(Uint32),
    "max_wait_time_for_late_members": Optional(Uint32),
    "unknown": Optional(Uint32),
    "max_group_radius": Optional(Float64),
    "min_group_radius": Optional(Float64),
    "max_member_speedup_when_behind": Optional(Float64),
    "max_member_slowdown_when_ahead": Optional(Float64),
    "max_group_slowdown_factor": Optional(Float64),
    "max_group_member_fallback_factor": Optional(Float64),
    "member_disown_distance": Optional(Float64),
    "tick_tolerance_when_member_arrives": Optional(Uint32),
    "max_gathering_unit_groups": Optional(Uint32),
    "max_unit_group_size": Optional(Uint32),
})

# https://lua-api.factorio.com/latest/types/PathFinderSettings.html
PathFinderSettings = Struct({
    "fwd2bwd_ratio": Optional(Int32),
    "goal_pressure_ratio": Optional(Float64),
    "use_path_cache": Optional(Bool),
    "max_steps_worked_per_tick": Optional(Float64),
    "max_work_done_per_tick": Optional(Uint32),
    "short_cache_size": Optional(Uint32),
    "long_cache_size": Optional(Uint32),
    "short_cache_min_cacheable_distance": Optional(Float64),
    "short_cache_min_algo_steps_to_cache": Optional(Uint32),
    "long_cache_min_cacheable_distance": Optional(Float64),
    "cache_max_connect_to_cache_steps_multiplier": Optional(Uint32),
    "cache_accept_path_start_distance_ratio": Optional(Float64),
    "cache_accept_path_end_distance_ratio": Optional(Float64),
    "negative_cache_accept_path_start_distance_ratio": Optional(Float64),
    "negative_cache_accept_path_end_distance_ratio": Optional(Float64),
    "cache_path_start_distance_rating_multiplier": Optional(Float64),
    "cache_path_end_distance_rating_multiplier": Optional(Float64),
    "stale_enemy_with_same_destination_collision_penalty": Optional(Float64),
    "ignore_moving_enemy_collision_distance": Optional(Float64),
    "enemy_with_different_destination_collision_penalty": Optional(Float64),
    "general_entity_collision_penalty": Optional(Float64),
    "general_entity_subsequent_collision_penalty": Optional(Float64),
    "extended_collision_penalty": Optional(Float64),
    "max_clients_to_accept_any_new_request": Optional(Uint32),
    "max_clients_to_accept_short_new_request": Optional(Uint32),
    "direct_distance_to_consider_short_request": Optional(Uint32),
    "short_request_max_steps": Optional(Uint32),
    "short_request_ratio": Optional(Float64),
    "min_steps_to_check_path_find_termination": Optional(Uint32),
    "start_to_goal_cost_multiplier_to_terminate_path_find": Optional(Float64),
    "overload_levels": Optional(Array(Uint32)),
    "overload_multipliers": Optional(Array(Float64)),
    "negative_path_cache_delay_interval": Optional(Uint32),
})

# https://lua-api.factorio.com/latest/types/DifficultySettings.html
DifficultySettings = Struct({
    "technology_price_multiplier": Float64,
    "spoil_time_modifier": Float64,
})

# https://lua-api.factorio.com/latest/types/AsteroidSettings.html
AsteroidSettings = Struct({
    "spawning_rate": Optional(Float64),
    "max_ray_portals_expanded_per_tick": Optional(Uint32),
})

# https://lua-api.factorio.com/latest/prototypes/MapSettings.html
MapSettings = Struct({
    "pollution": PollutionSettings,
    "enemy_evolution": EnemyEvolutionSettings,
    "enemy_expansion": EnemyExpansionSettings,
    "unit_group": UnitGroupSettings,
    "path_finder": PathFinderSettings,
    "max_failed_behavior_count": Uint32,
    "difficulty_settings": DifficultySettings,
    "asteroids": AsteroidSettings,
})


read_map_exchange_settings, write_map_exchange_settings = Struct({
    "map_gen_settings": MapGenSettings,
    "map_settings": MapSettings,
})


##########
# A test #
##########

assert parse_map_exchange_string(">>>eNp1Uj2LE0EYnrm4JubuvHAEQTjOFFpG8BRsJLsKIiJa2q6TzSQObmbifEROC1NYKjY22nitzXXClQeKaHfoHzix0UKJKNoIcWY3s9mP3MA7+8zzvvO8HzsLAIIVsADAWg3dVSRkfsBVB/uMhACMXGvlAIUBkTjNHQoYygRVAzYYYN5kPBN3JFJs5hSrmOL+ZrONRCZ4uRsqxgnF/hBTmfWosMc48oOQdLtpz4r1EBEi2hFp32IvxO05d2oxHxXh54tYip0DrSbnqQnJKJ7D30MS8zRfIZzR/DyWQyJvE9X326bPTF6K1JCIYrUOZ8GdTCWOCDgapJljQiIuCe35iGPk9xkRUmUzO4XC60KFXcVJ4KOAdPwe3hTZDhzJMc5kXpKK9oTE1M/1tag4orqvQr9DFQaIKt1X7sGsJp4hM4CIfiZ3YZ4AntpZfTt6tA6MTR6CxmRiTKN9ACIDcBRHQ03a5UwnChoXtV2ayUH4oL595fP9Zy6MI097UzCeMrtty1y14IZ3oOukBedSOhA++f566++7vRb89+rnx+vtWy48c7n+Y7yx3dJOxxRdMtvhBMV3921VFS/PaPDiuVnf3FigOrvW8ODWY33avVYCsFLWqHZUbxHXWEvCWla07sFutP648Gy0vljwqVCB7vCCSbVutvdmc2aZgaf7icFTD3onrPf4LETf3wDpGjrmFPfywaZ9k8qfK6Q44XQfOSYJrqRANKlOsn0tpee9V7Yn76UX/Qtgon7D6Z+JPFYq/tY8WNefUvLaxm72CRlgRHbO3/z1H+McJS8=<<<") == {
    "map_gen_settings": {
        "autoplace_controls": {
            "aquilo_crude_oil": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "calcite": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "coal": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "copper-ore": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "crude-oil": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "enemy-base": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "fluorine_vent": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "fulgora_cliff": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "fulgora_islands": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "gleba_cliff": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "gleba_enemy_base": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "gleba_plants": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "gleba_stone": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "gleba_water": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "iron-ore": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "lithium_brine": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "nauvis_cliff": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "rocks": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "scrap": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "starting_area_moisture": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "stone": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "sulfuric_acid_geyser": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "trees": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "tungsten_ore": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "uranium-ore": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "vulcanus_coal": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "vulcanus_volcanism": { "frequency": 1.0, "size": 1.0, "richness": 1.0 },
            "water": { "frequency": 1.0, "size": 1.0, "richness": 1.0 }
        },
        "autoplace_settings": {},
        "default_enable_all_autoplace_controls": True,
        "seed": 3289561125,
        "width": 2000000,
        "height": 2000000,
        "area_to_generate_at_start": {
            "left_top": {"x": -57344, "y": -57344},
            "right_bottom": {"x": 57344, "y": 57344},
            "orientation": {"x": 0, "y": -32767}
        },
        "starting_area": 1.0,
        "peaceful_mode": False,
        "no_enemies_mode": False,
        "starting_points": [{"x": 0, "y": 0}],
        "property_expression_names": {},
        "cliff_settings": {
            "name": "cliff",
            "control": "",
            "cliff_elevation_0": 10.0,
            "cliff_elevation_interval": 40.0,
            "richness": 1.0,
            "cliff_smoothing": 1.0
        },
        "territory_settings": None,
    },
    "map_settings": {
        "pollution": {
            "enabled": True,
            "diffusion_ratio": 0.02,
            "min_to_diffuse": 15.0,
            "ageing": 1.0,
            "expected_max_per_chunk": 150.0,
            "min_to_show_per_chunk": 50.0,
            "min_pollution_to_damage_trees": 60.0,
            "pollution_with_max_forest_damage": 150.0,
            "pollution_per_tree_damage": 50.0,
            "pollution_restored_per_tree_damage": 10.0,
            "max_pollution_to_restore_trees": 20.0,
            "enemy_attack_pollution_consumption_modifier": 1.0
        },
        "enemy_evolution": {
            "enabled": True,
            "time_factor": 4e-06,
            "destroy_factor": 0.002,
            "pollution_factor": 9e-07
        },
        "enemy_expansion": {
            "enabled": True,
            "max_expansion_distance": 5,
            "min_expansion_distance": 3,
            "friendly_base_influence_radius": 6,
            "enemy_building_influence_radius": 3,
            "building_coefficient": 0.5,
            "other_base_coefficient": 3.0,
            "neighbouring_chunk_coefficient": 0.5,
            "neighbouring_base_chunk_coefficient": 0.5,
            "max_colliding_tiles_coefficient": 0.8,
            "settler_group_min_size": 5,
            "settler_group_max_size": 10,
            "evolution_group_size_factor": 8.0,
            "min_expansion_cooldown": 36000,
            "max_expansion_cooldown": 216000
        },
        "unit_group": {
            "min_group_gathering_time": 1800,
            "max_group_gathering_time": 3600,
            "max_wait_time_for_late_members": 36000,
            "unknown": 7200,
            "max_group_radius": 30.0,
            "min_group_radius": 5.0,
            "max_member_speedup_when_behind": 1.4,
            "max_member_slowdown_when_ahead": 0.6,
            "max_group_slowdown_factor": 0.3,
            "max_group_member_fallback_factor": 3.0,
            "member_disown_distance": 10.0,
            "tick_tolerance_when_member_arrives": 60,
            "max_gathering_unit_groups": 30,
            "max_unit_group_size": 200
        },
        "path_finder": {
            "fwd2bwd_ratio": 5,
            "goal_pressure_ratio": 2.0,
            "use_path_cache": True,
            "max_steps_worked_per_tick": 1000.0,
            "max_work_done_per_tick": 8000,
            "short_cache_size": 5,
            "long_cache_size": 25,
            "short_cache_min_cacheable_distance": 10.0,
            "short_cache_min_algo_steps_to_cache": 50,
            "long_cache_min_cacheable_distance": 30.0,
            "cache_max_connect_to_cache_steps_multiplier": 100,
            "cache_accept_path_start_distance_ratio": 0.2,
            "cache_accept_path_end_distance_ratio": 0.15,
            "negative_cache_accept_path_start_distance_ratio": 0.3,
            "negative_cache_accept_path_end_distance_ratio": 0.3,
            "cache_path_start_distance_rating_multiplier": 10.0,
            "cache_path_end_distance_rating_multiplier": 20.0,
            "stale_enemy_with_same_destination_collision_penalty": 30.0,
            "ignore_moving_enemy_collision_distance": 5.0,
            "enemy_with_different_destination_collision_penalty": 30.0,
            "general_entity_collision_penalty": 10.0,
            "general_entity_subsequent_collision_penalty": 3.0,
            "extended_collision_penalty": 3.0,
            "max_clients_to_accept_any_new_request": 10,
            "max_clients_to_accept_short_new_request": 100,
            "direct_distance_to_consider_short_request": 100,
            "short_request_max_steps": 1000,
            "short_request_ratio": 0.5,
            "min_steps_to_check_path_find_termination": 2000,
            "start_to_goal_cost_multiplier_to_terminate_path_find": 2000.0,
            "overload_levels": [0, 100, 500],
            "overload_multipliers": [2.0, 3.0, 4.0],
            "negative_path_cache_delay_interval": 20
        },
        "max_failed_behavior_count": 3,
        "difficulty_settings": {"technology_price_multiplier": 1.0, "spoil_time_modifier": 1.0},
        "asteroids": {"spawning_rate": 1.0, "max_ray_portals_expanded_per_tick": 100}
    }
}

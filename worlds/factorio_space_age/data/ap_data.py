# This file is somewhat arbitrary constants chosen for the randomizer.
# This file is inputs to both import-ap-dump.py and also the apworld proper.

__version__ = "3.0.1"

# progressive_technologies: only_related
small_progressive_groups = {
    #"progressive-advanced-material-processing": [
    #    "advanced-material-processing",
    #    "advanced-material-processing-2",
    #],
    "progressive-armor": [
        "heavy-armor",
        "modular-armor",
        "power-armor",
        "power-armor-mk2",
        "mech-armor",
    ],
    "artillery-shell-damage": [
        "artillery-shell-damage-1",
    ],
    "artillery-shell-range": [
        "artillery-shell-range-1",
    ],
    "artillery-shell-speed": [
        "artillery-shell-speed-1",
    ],
    "asteroid-productivity": [
        "asteroid-productivity",
    ],
    "progressive-automation": [
        #"automation", # This is unrandomized.
        "automation-2",
        "automation-3",
    ],
    "braking-force": [
        "braking-force-1",
        "braking-force-2",
        "braking-force-3",
        "braking-force-4",
        "braking-force-5",
        "braking-force-6",
        "braking-force-7",
    ],
    "progressive-efficiency-module": [
        "efficiency-module",
        "efficiency-module-2",
        "efficiency-module-3",
    ],
    #"progressive-electric-energy-distribution": [
    #    "electric-energy-distribution-1",
    #    "electric-energy-distribution-2",
    #],
    "electric-weapons-damage": [
        "electric-weapons-damage-1",
        "electric-weapons-damage-2",
        "electric-weapons-damage-3",
        "electric-weapons-damage-4",
    ],
    "progressive-energy-shield": [
        "energy-shield-equipment",
        "energy-shield-mk2-equipment",
    ],
    "progressive-follower-robot": [
        "defender",
        "distractor",
        "destroyer",
    ],
    "follower-robot-count": [
        "follower-robot-count-1",
        "follower-robot-count-2",
        "follower-robot-count-3",
        "follower-robot-count-4",
        "follower-robot-count-5",
    ],
    "health": [
        "health",
    ],
    "progressive-inserter": [
        "fast-inserter",
        "bulk-inserter",
        "stack-inserter",
    ],
    "inserter-capacity-bonus": [
        "inserter-capacity-bonus-1",
        "inserter-capacity-bonus-2",
        "inserter-capacity-bonus-3",
        "inserter-capacity-bonus-4",
        "inserter-capacity-bonus-5",
        "inserter-capacity-bonus-6",
        "inserter-capacity-bonus-7",
    ],
    "laser-shooting-speed": [
        "laser-shooting-speed-1",
        "laser-shooting-speed-2",
        "laser-shooting-speed-3",
        "laser-shooting-speed-4",
        "laser-shooting-speed-5",
        "laser-shooting-speed-6",
        "laser-shooting-speed-7",
    ],
    "laser-weapons-damage": [
        "laser-weapons-damage-1",
        "laser-weapons-damage-2",
        "laser-weapons-damage-3",
        "laser-weapons-damage-4",
        "laser-weapons-damage-5",
        "laser-weapons-damage-6",
        "laser-weapons-damage-7",
    ],
    "progressive-logistics": [
        "logistics",
        "logistics-2",
        "logistics-3",
        "turbo-transport-belt",
    ],
    "low-density-structure-productivity": [
        "low-density-structure-productivity",
    ],
    #"progressive-military": [
    #    "military",
    #    "military-2",
    #    "military-3",
    #    "military-4",
    #],
    "progressive-mining-drill": [
        "electric-mining-drill",
        "big-mining-drill",
    ],
    "mining-productivity": [
        "mining-productivity-1",
        "mining-productivity-2",
        "mining-productivity-3",
    ],
    "progressive-personal-battery": [
        "battery-equipment",
        "battery-mk2-equipment",
        "battery-mk3-equipment",
    ],
    "progressive-personal-roboport": [
        "personal-roboport-equipment",
        "personal-roboport-mk2-equipment",
    ],
    "physical-projectile-damage": [
        "physical-projectile-damage-1",
        "physical-projectile-damage-2",
        "physical-projectile-damage-3",
        "physical-projectile-damage-4",
        "physical-projectile-damage-5",
        "physical-projectile-damage-6",
        "physical-projectile-damage-7",
    ],
    "plastic-bar-productivity": [
        "plastic-bar-productivity",
    ],
    "progressive-portable-power": [
        "solar-panel-equipment",
        "fission-reactor-equipment",
        "fusion-reactor-equipment",
    ],
    "processing-unit-productivity": [
        "processing-unit-productivity",
    ],
    "progressive-productivity-module": [
        "productivity-module",
        "productivity-module-2",
        "productivity-module-3",
    ],
    "progressive-quality-module": [
        "quality-module",
        "quality-module-2",
        "quality-module-3",
    ],
    "progressive-quality": [
        "epic-quality",
        "legendary-quality",
    ],
    "railgun-damage": [
        "railgun-damage-1",
    ],
    "railgun-shooting-speed": [
        "railgun-shooting-speed-1",
    ],
    "refined-flammables": [
        "refined-flammables-1",
        "refined-flammables-2",
        "refined-flammables-3",
        "refined-flammables-4",
        "refined-flammables-5",
        "refined-flammables-6",
        "refined-flammables-7",
    ],
    "research-productivity": [
        "research-productivity",
    ],
    "research-speed": [
        "research-speed-1",
        "research-speed-2",
        "research-speed-3",
        "research-speed-4",
        "research-speed-5",
        "research-speed-6",
    ],
    "rocket-fuel-productivity": [
        "rocket-fuel-productivity",
    ],
    "rocket-part-productivity": [
        "rocket-part-productivity",
    ],
    "scrap-recycling-productivity": [
        "scrap-recycling-productivity",
    ],
    "progressive-soil": [
        "artificial-soil",
        "overgrowth-soil",
    ],
    "progressive-speed-module": [
        "speed-module",
        "speed-module-2",
        "speed-module-3",
    ],
    "steel-plate-productivity": [
        "steel-plate-productivity",
    ],
    "stronger-explosives": [
        "stronger-explosives-1",
        "stronger-explosives-2",
        "stronger-explosives-3",
        "stronger-explosives-4",
        "stronger-explosives-5",
        "stronger-explosives-6",
        "stronger-explosives-7",
    ],
    "transport-belt-capacity": [
        "transport-belt-capacity-1",
        "transport-belt-capacity-2",
    ],
    "weapon-shooting-speed": [
        "weapon-shooting-speed-1",
        "weapon-shooting-speed-2",
        "weapon-shooting-speed-3",
        "weapon-shooting-speed-4",
        "weapon-shooting-speed-5",
        "weapon-shooting-speed-6",
    ],
    "worker-robots-speed": [
        "worker-robots-speed-1",
        "worker-robots-speed-2",
        "worker-robots-speed-3",
        "worker-robots-speed-4",
        "worker-robots-speed-5",
        "worker-robots-speed-6",
        "worker-robots-speed-7",
    ],
    "worker-robots-storage": [
        "worker-robots-storage-1",
        "worker-robots-storage-2",
        "worker-robots-storage-3",
    ],
}

# progressive_technologies: large_groups
large_progressive_groups = {

    "progressive-mining": [
        "electric-mining-drill",
        "mining-productivity-1",
        "mining-productivity-2",
        "mining-productivity-3", # infinite
    ],
    "progressive-oil": [
        "oil-gathering",
        "oil-processing",
        "sulfur-processing",
        "chemical-science-pack",
        "fluid-handling",
        "advanced-oil-processing",
        "coal-liquefaction",
        "fluid-wagon",
        "plastic-bar-productivity", # infinite
    ],
    "progressive-production": [
        "steel-processing",
        "steel-axe",
        "advanced-material-processing",
        "advanced-material-processing-2",
        "production-science-pack",
        "effect-transmission",
        "steel-plate-productivity", # infinite
    ],

    "progressive-logistics": [
        "logistics",
        "logistic-science-pack",
        "logistics-2",
        "logistics-3",
        "turbo-transport-belt",
        "transport-belt-capacity-1",
        "transport-belt-capacity-2",
    ],
    "progressive-inserter": [
        "fast-inserter",
        "bulk-inserter",
        "inserter-capacity-bonus-1",
        "inserter-capacity-bonus-2",
        "inserter-capacity-bonus-3",
        "stack-inserter",
        "inserter-capacity-bonus-4",
        "inserter-capacity-bonus-5",
        "inserter-capacity-bonus-6",
        "inserter-capacity-bonus-7",
    ],
    "progressive-circuit": [
        "plastics",
        "advanced-circuit",
        "automation-2",
        "processing-unit",
        "circuit-network",
        "automation-3",
        "quantum-processor",
        "advanced-combinators",
        "processing-unit-productivity", # infinite
    ],

    "progressive-robotics": [
        "engine",
        "lubricant",
        "electric-engine",
        "battery",
        "robotics",
        "utility-science-pack",
        "construction-robotics",
        "worker-robots-speed-1",
        "worker-robots-speed-2",
        "worker-robots-speed-3",
        "worker-robots-speed-4",
        "worker-robots-speed-5",
        "worker-robots-speed-6",
        "worker-robots-speed-7", # infinite
    ],
    "progressive-logistic-robotics": [
        "logistic-robotics",
        "logistic-system",
        "worker-robots-storage-1",
        "worker-robots-storage-2",
        "worker-robots-storage-3",
    ],
    "progressive-train-network": [
        "railway",
        "automated-rail-transportation",
        "elevated-rail",
        "rail-support-foundations",
        "braking-force-1",
        "braking-force-2",
        "braking-force-3",
        "braking-force-4",
        "braking-force-5",
        "braking-force-6",
        "braking-force-7",
    ],
    "progressive-uranium": [
        "planet-discovery-nauvis", # for any-planet-start mod.
        "uranium-mining",
        "uranium-processing",
        "nuclear-power",
        "uranium-ammo",
        "kovarex-enrichment-process",
        "nuclear-fuel-reprocessing",
    ],

    "progressive-space": [
        "concrete",
        "low-density-structure",
        "rocket-fuel",
        "rocket-silo",
        "space-platform",
        "space-science-pack",
        "space-platform-thruster",
        "advanced-asteroid-processing",
        "asteroid-reprocessing",
        "asteroid-productivity", # infinite
    ],
    "progressive-vulcanus": [
        "planet-discovery-vulcanus",
        "tungsten-carbide",
        "foundry",
        "big-mining-drill",
        "tungsten-steel",
        "metallurgic-science-pack",
        "calcite-processing",
        "cliff-explosives",
        "artillery",
        "low-density-structure-productivity", # infinite
    ],
    "progressive-gleba": [
        "landfill",
        "planet-discovery-gleba",
        "yumako",
        "biochamber",
        "jellynut",
        "bioflux",
        "agriculture",
        "agricultural-science-pack",
        "bacteria-cultivation",
        "bioflux-processing",
        "artificial-soil",
        "overgrowth-soil",
        "rocket-fuel-productivity", # infinite
    ],
    "progressive-fulgora": [
        "electric-energy-accumulators",
        "planet-discovery-fulgora",
        "recycling",
        "holmium-processing",
        "electromagnetic-plant",
        "electromagnetic-science-pack",
        "lightning-collector",
        "scrap-recycling-productivity", # infinite
    ],
    "progressive-aquilo": [
        "planet-discovery-aquilo",
        "lithium-processing",
        "cryogenic-plant",
        "cryogenic-science-pack",
        "rocket-part-productivity", # infinite
    ],
    "progressive-promethium": [
        "railgun",
        "stellar-discovery-solar-system-edge",
        "promethium-science-pack",
        "research-productivity", # infinite
    ],

    "progressive-captivity": [
        "captivity",
        "biter-egg-handling",
        "biolab",
        "captive-biter-spawner",
    ],

    "progressive-military": [
        "military",
        "gun-turret",
        "stone-wall",
        "military-2",
        "military-science-pack",
        "physical-projectile-damage-1",
        "weapon-shooting-speed-1",
        "physical-projectile-damage-2",
        "weapon-shooting-speed-2",
        "military-3",
        "physical-projectile-damage-3",
        "weapon-shooting-speed-3",
        "physical-projectile-damage-4",
        "weapon-shooting-speed-4",
        "military-4",
        "physical-projectile-damage-5",
        "weapon-shooting-speed-5",
        "physical-projectile-damage-6",
        "weapon-shooting-speed-6",
        "physical-projectile-damage-7", # infinite
    ],
    "progressive-explosives": [
        "explosives",
        "rocketry",
        "land-mine",
        "stronger-explosives-1",
        "stronger-explosives-2",
        "explosive-rocketry",
        "carbon-fiber",
        "rocket-turret",
        "stronger-explosives-3",
        "stronger-explosives-4",
        "stronger-explosives-5",
        "stronger-explosives-6",
        "atomic-bomb",
        "stronger-explosives-7", # infinite
    ],

    # These are unchanged:
    **{k: small_progressive_groups[k] for k in [
        "progressive-efficiency-module",
        "progressive-productivity-module",
        "progressive-speed-module",
        "progressive-quality-module",
        "progressive-quality",

        "research-speed",

        "progressive-armor",
        "progressive-portable-power",
        "progressive-personal-battery",
        "progressive-personal-roboport",
        "progressive-energy-shield",
        "progressive-follower-robot",

        "artillery-shell-damage",  # infinite
        "artillery-shell-range",   # infinite
        "artillery-shell-speed",   # infinite
        "electric-weapons-damage", # infinite
        "follower-robot-count",    # infinite
        "health",                  # infinite
        "laser-shooting-speed",    # infinite
        "laser-weapons-damage",    # infinite
        "railgun-shooting-speed",  # infinite
        "railgun-damage",          # infinite
        "refined-flammables",      # infinite
    ]},
}

energy_link_bridge_recipes = {
    "early_game": [
        dict(type="item", amount=50, name="iron-plate"),
        dict(type="item", amount=50, name="copper-plate"),
    ],
    "mid_game": [
        dict(type="item", amount=1, name="accumulator"),
        dict(type="item", amount=1, name="radar"),
    ],
    "fulgora": [
        dict(type="item", amount=10, name="supercapacitor"),
        dict(type="item", amount=1,  name="radar"),
    ],
}

# These are critical at the start.
# The fill algorithm crumbles if you let it attempt to random a way out of the early game.
starting_planet_to_unrandomized_technologies = {
    "nauvis": {
        # Labs and red science:
        "steam-power",
        "electronics",
        "automation-science-pack",
        "automation",
    },
    "vulcanus": {
        # Labs and red science:
        "solar-energy",
        "electronics",
        "automation-science-pack",
        "automation",
        # Foundries require all of this:
        "steel-processing",
        "oil-gathering",
        "oil-processing",
        "lubricant",
        "calcite-processing", # chemical plant and water
        "concrete",
        "automation-2", # crafting with fluid
        "tungsten-carbide",
        "foundry",
        # And now you can automate iron and copper!
    },
    "gleba": {
        # Labs and red science:
        "steam-power",
        "electronics",
        "automation-science-pack",
        "automation",
        # Bacteria cultivation requires all of this:
        "steel-processing",
        "landfill",
        "agriculture",
        "biochamber",
        "yumako",
        "jellynut",
        "bioflux",
        "bacteria-cultivation",
        # And now you can automate iron and copper!
    },
    "fulgora": {
        "recycling", # scrap recycling and recyclers.
        "battery",   # accumulators
        # Labs and red science:
        "electronics",
        "automation-science-pack",
        "automation",
    },
}

never_give_free_samples_from_recipes = {
    # Originally derrived from the .hide_from_player_crafting recipe prototype property.
    # See also: https://github.com/thejoshwolfe/Archipelago/issues/10
    # Also includes all recycling recipes (other than scrap recylcing).
    "rocket-part",
    "biter-egg",
    "empty-crude-oil-barrel",
    "empty-fluoroketone-cold-barrel",
    "empty-fluoroketone-hot-barrel",
    "empty-heavy-oil-barrel",
    "empty-light-oil-barrel",
    "empty-lubricant-barrel",
    "empty-petroleum-gas-barrel",
    "empty-sulfuric-acid-barrel",
    "empty-water-barrel",
    "crude-oil-barrel",
    "fluoroketone-cold-barrel",
    "fluoroketone-hot-barrel",
    "heavy-oil-barrel",
    "light-oil-barrel",
    "lubricant-barrel",
    "petroleum-gas-barrel",
    "sulfuric-acid-barrel",
    "water-barrel",
}

# The `intermediate_technologies: unlocked` option starts you with these technologies unlocked.
intermediate_recipe_technologies = {
    "engine",
    "oil-processing", # Unlocks solid fuel from petroleum, otherwise it's not directly useful without oil-gathering (pumpjacks).
    "sulfur-processing",
    "plastics",
    "advanced-circuit",
    "explosives",
    "battery",
    "lubricant",
    "electric-engine",
    "robotics", # flying-robot-frame
    "low-density-structure",
    "processing-unit",

    # centrifuges do nothing without uranium ore (seperate unlock) and something to do with the processed uranium.
    "uranium-processing",

    "jellynut", # You can eat it, but that doesn't count as useful enough to make it a multiworld item.
    "yumako",   # Same as above.
    "bioflux",  # Same as above.
    "carbon-fiber",
    # "bioflux-processing", # Unlocks alternative sources for several resources.
    # "bacteria-cultivation", # Unlocks alternative metal sources.
    # "calcite-processing", # Unlocks acid power for Vulcanus.
    "holmium-processing",
    "tungsten-carbide",
    "tungsten-steel",

    "biter-egg-handling",
    "lithium-processing",
    "quantum-processor",
}

ap_item_names = [
    "ap-energy-link-bridge",
    "victory",
]

trap_names = [
    "Artillery Trap",
    "Atomic Cliff Remover Trap",
    "Atomic Rocket Trap",
    "Attack Trap",
    "Cluster Grenade Trap",
    "Evolution Trap",
    "Grenade Trap",
    "Inventory Spill Trap",
    "Teleport Trap",
]


map_exchange_strings = {
    # Builtin
    "default": ">>>eNp1Uj2LE0EYnjGuibkPgwRBOM4UthE8r5TsKoiI6F9YJ5tJHNzMxPmInBZeYanY2GjjtTZnZWN1IIh2h/6BiI0WagTRRogzu5nNzu458M48+zzvvF87hwAEq9rAWgPdViRmYcRVD4eMxABs+9aqEYojInGeOxwx5DjVIzYaYd5m3PE7mkRsFyLWMcXDrXYXCcd5pR8rxgnF4RhT6SoqHjCOwigm/X5eOWYVImJEeyKvLQ1i3D3gTiPlkyLCYhHLqTjS0eRB0YRkFB/A30ES8zxfI5zR4jxWYiJvEjUMu6ZPJy9FakxEuVqPs+iWU4knIo5GeeaEkIhLQgch4hiFQ0aEVG5mr1R4U6i4rziJQhSRXjjAW8LtwJMcYyfzslR0ICSmYaGvJcUR1X2V+h2rOEJU6b4KD+Z4poyZAUQMndyleZqHqs8H64nN7oPWbGZMo4kWjAG4nXpDTdrlzScKWhe0XVyEg/Bec/fyp7tPfJh6ngnmYDpn9rqWuWLB9eC/0mkLNnNxIHz07dXOn7f7Hfj3xc8P17o3fHj2UvP7dGO3o0XPFF0x25EMpXcntqpaUGQ0ePbUrK9+GqC+uNYK4M5D/bV3tQJgrapRY1VvCdday9w6NmgzgP1k/fbhuWR9tuBjqQLd4XmTat1s78zmLTKDQPeTgscBDE5Z9eTCRd/fAPkaeuYr7eW9Tfsml79QSHnC+T4KTOZcy4FkUr1s+1LJz3u/ar+C50HyL4Dx+gXnfyZRbKj0bASwqY9K9tqmvvuEDDBBfrx+OfkHMfYkeg==<<<",
    "rich_resources": ">>>eNp1Uk2LUzEUTay1db4sUgRhGLtwW8FxltIXhUFE9C8809e0Bl+Tmo/K6MIuXCpu3OhCZ+tmdu4HBNHdoGthxI0ulAqiG6Em7zVt0tbATU7OvTn33iRHAARrxsB6Bd/RNOVxInSLxJymAAwiZ6UEpwlVxOeOJhx7QQAtJbzXI6LOBfHp45liPVA0wYSR7k69iWUgutpONReUkbhPmAo9Ou1wgeMkpe227znhPFSmmLWk71vupKS54Ewl57Mi4tkiVnJnz6ipRWpScUYW8HexIsLny1RwNnsfqylVt6juxk3bZ5CXYd2ncr7aouDJ7aCSokwE7vnMKamwUJR1YiwIjrucSqUFCQ+FhQNUlTpta0GTGCe0FXfIjgw7KCpBSJB5RWnWkYqwmIfqy1pgZvqa67ev0wQzbfoKPswgOjnx9LkFVHaD3HP3aT+qWR9uZDZ6AGqjkTWDDo3DGoCDPBoa0h+1S8YuT5UgvF/du/L53tMI5gHn0BgMx8x+0zFXHbiB/us668CWpwPh4++vd/+8PWjAv69+frjevBnB89vVH8PNvYZxFm29BTsdm6D87KGrqoxmGQOeP7PjW5QLLE2P1RDcfWR2+9cKAJZLBlXWzJRxtfVJWMOJVhFsZ+N3BC9k44sDH+cqMB1etKk27PTOTsVpZoBMPzl4giA647ynpyHm/Cbwa2jZXd7Le5f2jZd/ppD5G/b7mGEmwWUPZDfVmkxfC/59H5TcDr1E2VsAG/ULjl8m8zipfK0gWDVLYfLJhlH4hSywIpvbn178A09AHjE=<<<",
    "marathon": ">>>eNp1Uk2LEzEYnljH1nZ3LVIEYVl78FrBdY/SRkFERf/CmE4zNThNaj4qqwcX8ah40Ite3KuXvXlfEERvi/6BFS96UFYQvQg1mWmmmZkaeJMnz/Pm/UhyyAPeijZvtYnuKBKzIORqgANGYs/b6lmrhigOicQudzhkKOdUD9l4jHmH8Zzf0SRipxCxjikebXb6SOScl6NYMU4oDiaYyryi4iHjKAhjEkWucswqRMSIDoSrNYYx7i8400z5pIigWMRSKo51NLkompCM4gX8XSQxd/ka4YwW72M5JvIWUaOgb/rM5aVITYgoV+tzFt7OVeKLkKOxy5wQEnFJ6DBAHKNgxIiQKp/ZLxXeEiqOFCdhgEIyCIZ4U+Q78CXHOJd5SSo6FBLToNBXQ3FEdV+lficqDhFVuq/ChzmeKRNmABGjXO7SfZqPqtdHa4lNH3jt6dSYRvtaMOaBrdQbaNId7QvaLs4jAXC/tXP5873nPZA6nIEzcDBjdvuWuWLBDfhf6bQFG04cAJ58f7P9591eF/x9/fPj9f7NHjh7qfXjYH2nq0Xf1Fsx05EMpWf3bVU1WGQ0ePnCjG+9NEB9fqwNwfZjvdu9VvFArapRc0VPCddezdy6NmgLgigZv3vgXDK+WPCpVIHu8LxJtWam92by55k9qPtJwVMI4Cmrnpy76PPrnlvDwOzSXj7YtG+d/IVCyjfs9lFgMueaA5KbGmTT14p733tVu4OvYPIWnvH6BWYvkyg2VLo2IWjppZJ9sibMfyEDTJDGw6vP/gHlbh/E<<<",
    "death_world": ">>>eNp1VL+LE0EUnrm4XsxdziBBEI4zwrWxUEvJrjYiorXdOtnM5gY3M3F+RE6LC5yFhaCFjTbaCmKl/YGNdqL/wMk1auVBFAshzuxmN7O7ceC9+ea9N+997+2wSwCCNS1gvYHuKBIxP+Cqh31GIgDGbirLAYoCIrFtOxIwlAuqBWw4xLzNeC7uWJyxXchYwxQPtttdJHQw8BIZu/UwUowTiv0RptK+UA9V1Gcc+UFEwtD2HE89RESI9oTtW+lHuLvgTiOxxyT8hMTcuZo4hzqbXJRNSEbxAvtdJDG37VXCGS3Oox4RuUXUwO+aPnN1KVIjIspsHc6C2zkmjgg4GtqWk0IiLgnt+4hj5A8YEVLlKzsl4k2holBxEvgoID2/j7dFvgNHcoxzlVelon0hMfULfa0ojqjuq9TvSEUBokr3VXgwJzLPiBlAxCBXuzRP81D1/mAjlukOaE2nRjTa1w4jAI71U9LRUBvt1bqk5fI8E4T3m2+ufL331IVJwFlvBvZnlr1uarmaghvef12bKbhg5YHwcOvg4bs/kw78++rw8/XuLReOduuTX2fedrTTMXwrRh3NUJ4DqBZZGfD8mVnf3SRBbX6t5cGXj/Rp71oFwJtLGjXWtIptrfUsrJMmbXowjNdvF56P10EKvpQY6A4vmlIbRn0wyplXBp7uJwGPPeidTr2n5iH6/jlgc+iZU9LLx7Tse6t+gUh5wnYfBUsWXLVAPKlepr5V7Hl/Wk5P3gsv/hbARE3g7MuA2X8qTpXsDQ829VbJHtlPN91hBkySzR+vn/wDtf4g9Q==<<<",
    "death_world_marathon": ">>>eNp1VL+P0zAUtq+EK73rEaEKCenu6MBaBmBEjWFBCN1tSGzBTZ1iXeoU/yg6GOjAwABiYYGFW1kQC/tJSAg2BP/AIRYYECAhWJCKnTSpkxRLz/78vuf3vudYWQIQrGkD6y6+qWgU+wFXfeLHNAJg4mW2HOAooJLYvkNBjAtBjSAejQjvxLwQdyTJ2CllbBBGhrudHhY6GKDUJl4zjFTMKSP+mDBpH2iGKhrEHPtBRMPQZo5mDBURZn1hcyuDiPQWnHFTfyLCT0XMydWUHOlsclE2IWNGFvhvYUm47a9THrPyfTQjKm9QNfR7ps9CXYbVmIqqWofHwU5BiSMCjke257iQmEvKBj7mBPvDmAqpipWdivCWUFGoOA18HNC+PyC7otiBIzkhhcqrUrGBkIT5pb5WFMdM91Xpd6yiADOl+yo9mGM5M44NoGJYqF25T/NQ9XpvM7HpXdCeTo1pdKAJYwBO9FPS0VA77dG+oO3iPBOEd1ovLn26/diDacBpNAMHM89+L/NczsA2+i91KgPnEHz6xIyvni5CN65uuep7F/59/vPDVu+6Bx9+e7X3583LriYdo7dmpsM5KmoA9bIqA/L8SYLG/Fgbwb0Herd/pQbgtSWN3DU9Jb72eh7WzZK2EAyT8duDZ5PxOQMfKwp0h+dNqU0zvTWTM68MkO4nBY8QRCcz9sQ8RJ8/A2wNfbNLe3mXlX1t1S8JsW+42kfJkwfXLZDcVD+fvtTs+36/nO3QM5R8C2CifsHZlwGz/1SSKl1dBFt6qeWPzJ0RPzLNGpgkGzvb9/8BWFIheQ==<<<",
    "rail_world": ">>>eNp1Us+LEzEUTqy1dX9ZpAjCsvbgtYKrR2mjICKi/8KYTtMaTJOaH5XVg3vwqHjxogfdqyvsQfDkpSCI3kT/gRUvCioVRC9CTWaaaaZdAy/z5Xvvfe+9TPYBCFasgdUKvmEoE1EsTZtEgjIANpveSjFmMdUk5PbHArPn29sNABByxEIs+n0i60KSkD6YKNatYi6YcNLbqLewyokud5gRknISDQjXeY9hXSFxFDPa6YSeQ95DFcO8rULfYpeR1h45lZRPmohmm1hKnX2rpvdSU1pwsgd/E2siQ75MpeCz97HMqL5GTS9quTlzdTk2A6rmuy1KEV/PdVJUscT9kDmiNJaa8m6EJcFRT1CljST5JNd42EtVGdYxksYRjmk76pINlZ+gqCUhucpL2vCu0oRHIq++aCTmdq65eQeGxZgbO5d9MGHG4cwzEA5Q1cvVntwnsKdhytqHar931xIb3wG18diZRbvW4QzAzTQfWjJctbPWzmX6EMLb1Z0Ln249bMI04ASagNGEGbY8c9GDK+i/ruMenA50ILz//eXWnzfDBvz77OeHy62rTXjyfPXHaH2nAQEsun4LbjuQoTR313dVRrOMBY8fufW1mQosTNNqCG7ds6fhpQKA5ZJFlRW7JVxtNQtreNEqgp1k/W7CU8n67MHHuQ7shGdcqTW3vXVbcVoZIDtsCh4giI5579FpiM1fB2EPbXdKZ3nny74O6s80Mn/D4RwzTBZcDkByU+1s+1II7/t9yZ/QU5T8C+CifsHJn0k8Xir9VhCs2k8he2SjZv4JOeBEXrz69uQfWMEpWQ==<<<",
    "ribbon_world": ">>>eNp1Ur1rlDEcTlrPXr8POaRCqTe4VmjrKHdRECmi/0LMvZe7huaSMx8n1cEOjoqLiy7W0aWbe0EQuxX9ByouOigVRBehJu97eS/vtQaSPHme32eSMQDBnJtgsULuWcYlTpRtUSwZB2C7EeZEQnjCDI25M4kkzgghAIAjAJpKZK9H1bJUNKYn04jLacTImAra3VpuEl0IOtvmViomKO5TYYqK5R2pCE44a7djZT4oTHMiWjrWpjucNk/xqWR8WgQeLWImE3sumjktmjZS0FP4+8RQFfNlpqQYvY9ZzswGs13c9H0W8gpi+0zn1daddSqUlEw2C5WUdKJIL2bOa0OUYaKDiaIEdyXTxipadMoKH9ZS1Za3rWIJJglr4Q7d0sUOSkZRWsg8Y6zoaEMFlsXo01YR4fo60W/f8oQI6/pKP8zQ41yu9KUHTHcLucN9ouwuHOs+qtsfL4Fttx8/ArXjYz8dOnSEnwBuZ8mhIwdjbJJy2ieGSTGfI8zJJtULaX+47WrWBveI2cCJNdIauOI9a9fcvJ4XBSF8WN29+fnB8wbMQl9GA3A0YPaagVkP4A76r3QpgCtRHAiffn+78+f9QR3+ffPz4+3m3QZcuVH9cbS6W3diyTc57pezOcp8D0NVZTTKOPDyhR/fGlmAqaFbDcGdJ+60d2scwPKEQ5U5t6RcbTE3q4egVQTb6fjdgGvp+BLApxMVuA6v+lRLfvngl9IwM0Cunww8QxBdDOqFoYnzXwVxDS1/ynrZD2nfRflHCjl5w3EfI0xuXI5AelOtfPk6Ht/3wUQ4oVcofQvgrX7BwcukSgiV7RUEq24Lqn/y4hfywAd5vbC//g+6Lyzz<<<",
    "lakes": ">>>eNp1Us1rkzEYf2Pt1nVuK1JEYcweBE8TtnmU9lUQEdGT95imebuwNOnyUZ0K7uBR8eJFL+7qZTfvA0H0NvQfmHjRgzJB9CLU5H2bvh+dgSf55fk9eT5zLADBvJVgsYY2DWUCYmk6BArKgmC75WUaI4apJlndcSxQzqiKRb9P5LKQObuZ2ONywWOVcNLbWm4jlTOei5gRknICB4TrPGNYV0gEMaNRlGUWPEMVQ7yjstxsl5H2EW9qiT5OAhaTOJGQfetNH+VNacHJEfq7SBOZ1VeoFLzYjzlG9To1Pdh2debicmQGVE1mW5YCb+QyKSssUT+rOaU0kpryLkSSINgTVGmTj1yeSLyuDIuMpBgiTDuwS7ZUvoKyloSMIgdJktrwrtKEw0Jds0YibuuaqHdgGEbc2LoKH+bkmBkIB6jq5WJP9NN9VHs+Xopl+ChoDIdOLDqwhJMAbCfWwCpHa6qEzL0ZK27SFC/E/YWEkQHSVPClwh1GUvTSazWm7aiUqqUwcTUztlpInzO0QVTFD2Deg+TF6bihMLJNUhr2kV6H2GhhNFhxqTYuW7mS1gvAg/rutc/3n7dAUsuFcAQOR5q9ttdc9+BW+F/qnAcXM34AePr9zc6fd/tN8Pf1z48323daYOVq/cfh6m7TkmXX1ZLbpsYoeXvgs6qERY0FL1+49a2VOKimzxoh2Hlib3s3SgGoTFtUm7dbrGssjs2a3mk9BFG8frfAWry+ePBpIgNb4SUXaslt791WTiMHoa0nAc9CEJ717JnUxL5fDbI5dNwtqeWDD/s2E7+QyGSHs3UUNGPjSgbEneqMt6+lbL/3p/0tfBXGswic1S8wmkzMeFfJWQtB3R6edSPPfyEHnJPztx+u/QN71WBd<<<",
    "island": ">>>eNp1Us1rkzEYf2Pt1nZuK1JEYdQevE7Y5lHWV0FERP+FmKZ5u+DbpOajOgXdwaPixYu7uKsgu3kfCKK3of/AxIselAmiF6Emb5q+H52BJ/nl+T15PnMsAMGCkWCpju5oGnOIhe4SyGkcBFttL7MYxZgqktUdxxzljGqYDwZELHORs6smHpcLHmuEkf7mcgfJnPF8FGsuKCNwSJjKMzrucYEgjmkUZZlFz1AZI9aVWW6uF5POEW/qTp8kAYtJnHDkwHhTR3mTijNyhP4uUkRk9RUqOCv2Yz6maoPqPuzYOnNxGdJDKqezLQuOb+cyKUss0CCrOSUVEoqyHkSCINjnVCqdj1yeSrwhdRxpQTFEmHZhj2zKfAVlJQgZRw5ckkqznlSEwUJdc1ogZuqaqneoY4yYNnUVPszJCTPkFlDZz8We6qf9qOZ83Exk9ChojUZWDDowhJUAbDlrYJTjNVNC+l7ViJ00xYtJfyGJyRApylmzcIeR4P30WktoMyop6yl0rqoTq3r63H3Dip/AggfuyemkozAyXZIKDpDagFgrrhVYsbm2Lhm5nBYMwIPG7tXP95+3gSvmfDgGh2PNXsdrrnlwM/wvdc6DCxk/ADz9/mbnz7v9dfD31c+PNzq32mDlSuPH4eruuiHLtq0lu81MkHt74LOqhEWNAdsv7PrWdg5q6bNWCHaemNve9VIAKrMG1RfMluhaSxOzde+0EYIoWb/bYC1ZXzz4NJWBqfCiDdW023u7ldPIQWjqceBZCMKznj2Tmpj3q0E2h669uVo++LBvM/ELiUx3OFtHQTMxrmRA0qnuZPtayvZ7f9bfwpdhMovAWv0C48kkjHflznoIGubwrB15/gtZYJ2MXj/c/geh5mJi<<<",

    # Defined by this apworld
    "buffed_resources": ">>>eNp1Uj2LE0EYnjGuibnkDBIE4ThTWAkRPC0sJLsKIiL6F/Ymm9k4uNmNMzuR08ItbATFxkYbr1XhOvuAINod+gdObLRQIog2QpyP3c3s5hx4Z5553+f9nDkAIFgVAtZa6DYnQeR6lA+wG5EAgKmTSdVDgUdibOoOehEqkOpeNB5j2o1ogXdYReyWItZxiEdb3T5igpz0hMoWp930Ax5REmJ3gsPYdGj6PBhGFLleQHxfcoFaiX0ksxAWoHDAXr861dNeib0yDHB/H5+W1qsi3LQIWxeS2A1tHIto8X7RWByFhRZT/R0UYyr52iexa4RGYXkezYDENwkfuX3Zp2lphIhPCFuu1qKRd4ulJSqxmEfR2HQ+xmJEYxIOXUQxckcRYTGnuOhULrzNeOBzSjwXeWTgDvEWw9QkWDHFuJC5EfNwyGIcuqW+VjhFoehrqd8JDzwUctFX6cMczS2TSALCRua0LTXPdA46P1TzeLCuZH4fdOZzKQLtCYMUABPNhEJprs5FIZfyTiCA99o7Vz7ffWpDTTjtpGCWaqb9THM1Azec/5pOZuCcEQfCx9/fbP95t9uDf1/+/Hi9v2nDM5fbP2YbOz1htGS9FbkdypH23cuqqjlljQDPn8n1zdYB6gu3jgO3H4nb9FoFwFpVoNaq2JSus5bTelnQtgN9tX7b8KxaXzLwaakC0eEFmWpdbu/lZi0yA0f0o8ETBzonMuvxBUX4bwCzhoG86V4+ZGnfGvlLhSxP2OyjpMnJNQOoSQ3y7WvFnPduNbs5Lxz1FkCyfsH0ZZQlC6XPlgPb4qjkn2xmF7+QBDJIdfP8w38lRS8I<<<",
}

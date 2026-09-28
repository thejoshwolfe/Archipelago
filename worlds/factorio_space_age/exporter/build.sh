#!/usr/bin/env bash

set -e

starting_planet="$1" # Or nothing

version=$(jq -r .version archipelago-extractor/info.json)

rm -f archipelago-extractor/{settings-updates,template_parameters}.lua
if [ -n "$starting_planet" ]; then
    cp ../data/mod/settings-updates.lua archipelago-extractor/
    echo 'PARAMS = {
        starting_planet = "'"$starting_planet"'",
        vulcanus_rock_multiplier = 1,
        space_platform_foundation_amount_per_craft = 1,
        ice_platform_amount_per_craft = 1,
        refined_concrete_amount_per_craft = 1,
        heat_pipe_amount_per_craft = 1,
    }' > archipelago-extractor/template_parameters.lua
fi

rm -f archipelago-extractor_*.zip
zip -rq archipelago-extractor_"$version".zip archipelago-extractor/
echo archipelago-extractor_"$version".zip

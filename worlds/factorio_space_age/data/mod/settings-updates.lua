require "template_parameters" -- defines PARAMS

local function force_setting(setting_type, setting_name, value)
    local setting = data.raw[setting_type][setting_name]
    setting.hidden = true
    if setting_type == "bool-setting" then
        setting.forced_value = value
    else
        setting.allowed_values = {value}
        setting.default_value = value
    end
end

-- Configure any-planet-start settings.
-- We want:
--  * enable safe orbit
--  * enable vulcanus-fulgora space connection
--  * configurable vulcanus rock multiplier
-- The APS settings were determined by extracting the mod zip version 1.1.28 and reading settings.lua.
-- Factorio settings API reference is here: https://wiki.factorio.com/Tutorial:Mod_settings .
if mods["any-planet-start"] then
    local starting_planet = PARAMS.starting_planet
    if starting_planet == "nauvis" then starting_planet = "none" end -- It's called "none" I guess.
    force_setting("string-setting", "aps-planet", starting_planet)
    force_setting("bool-setting", "aps-safe-orbit", true)
    force_setting("double-setting", "aps-vulcanus-rock-multiplier", PARAMS.vulcanus_rock_multiplier)
    force_setting("bool-setting", "aps-vulcanus-fulgora", true)
end

-- Configure aquilo-orbit-start settings.
if mods["aquilo-orbit-start"] then
    force_setting("bool-setting", "aos-squeak-through", true)
    force_setting("bool-setting", "aos-space-platform-foundation-from-carbon-enabled", true)
    force_setting("int-setting",  "aos-space-platform-foundation-result-amount", PARAMS.space_platform_foundation_amount_per_craft)
    force_setting("bool-setting", "aos-space-platform-starter-pack-early", true)
    force_setting("bool-setting", "aos-cargo-bay-early", true)
    force_setting("int-setting",  "aos-ice-platform-result-amount", PARAMS.ice_platform_amount_per_craft)
    force_setting("int-setting",  "aos-refined-concrete-from-calcite-result-amount", PARAMS.refined_concrete_amount_per_craft)
    force_setting("int-setting",  "aos-heat-pipe-result-amount", PARAMS.heat_pipe_amount_per_craft)
    force_setting("bool-setting", "aos-aquilo-ocean-destroys-items", true)
    force_setting("bool-setting", "aos-electric-furnace-from-refined-concrete-enabled", true)
end

#!/usr/bin/env bash

set -e

starting_planet="$1" # Or nothing
FACTORIO_PATH=~/software/factorio # Or whatever path
ANY_PLANET_START_PATH=$(ls ~/.factorio/mods/any-planet-start_*.zip)

# This is just some default settings seed.
EXCHANGE_STRING='>>>eNp1Ur2LE0EUnzGuibkPgwRBOM4IYneCp6VkV0FERP8E18lmNg5uZuJ8RE4LU1gqNjYK4rU219kfCKLYHFranNpooUQQbYQ4s5vZ7Edu4M3+5vfevPd7b2cfgGBZG1hpoNuKRMwPuOpin5EIgJFrrRqgKCASZ7n9AUO5oHrABgPM1xjPxR2MM64VMtYxxf2NtQ4SueClMFKME4r9IaYy71FRj3HkBxEJw6znkPUQESHaFVnfQi/CnTl3Ggkfi/CLIhYT50Bnk/OyCckonsPfQRLzLF8jnNHiPJYiIm8S1fc7ps9cXYrUkIiyWoez4FZOiSMCjgZZ5oiQiEtCez7iGPl9RoRU+cpOSXhTqChUnAQ+CkjX7+ENke/AkRzjXOVFqWhPSEz9Ql8LiiOq+yr1O1RRgKjSfRUezOHUM2QGENHP1S7NE8Dnn74cHz1YBcYm90FrMjGm0S4AsQE4SqKhJu1yphMFrfPaLszSQXivuXXp890nLkwiT3lTMJ4y2x3LXLbgmren64QFZzN5IHz049Xm3zc7bfjv5a8PVzs3XHj6YvPneH2rrZ2OEV0x24EUJXd3raqaV2Q0ePbUrO9ukqA+u9by4OZDfdq+UgGwVtWosay3mGutpGFtm7TpwTBef1x4Jl5fLfhYUqA7PGdKrZrtrdmcWWXg6X4S8NiD3jHrPToL0ffXQVZD15ySXt7Zsq8z9QtCyhPO9lFg0uBaBsST6qbbt0p23jtVe/JeePG/ACbqN5z+mdhjUyXfhgeb+lNJX9vYzT8hA0yS9+HJ6/8B/m4lcg==<<<'

./build.sh "$starting_planet"
rm -rf mods/ && mkdir mods/
mv archipelago-extractor*.zip mods/
if [ -n "$starting_planet" ]; then
    cp "$ANY_PLANET_START_PATH" mods/
fi

rm -rf "$FACTORIO_PATH"/saves/archipelago-extractor-temp
"$FACTORIO_PATH"/bin/x64/factorio --mod-directory "$(cd mods/ && pwd)" --create       "$FACTORIO_PATH"/saves/archipelago-extractor-temp --exchange-string "$EXCHANGE_STRING"

echo -n '/ap-get-info-dump' | gtkclip # copy this to clipboard
"$FACTORIO_PATH"/bin/x64/factorio --mod-directory "$(cd mods/ && pwd)" --start-server "$FACTORIO_PATH"/saves/archipelago-extractor-temp
rm -rf "$FACTORIO_PATH"/saves/archipelago-extractor-temp

# Then paste the above.
# Then type /quit and hit Enter.

# factorio/data

How to recreate all the data:

0. Delete `*.json` from this directory.
1. See ../exporter . There's a bunch of steps there to run factorio and export some data. The result is a file `ap-dump.json`.
2. Run `./import-ap-dump.py .../path/to/ap-dump.json`.
3. You may be prompted by `./import-ap-dump.py` to run through steps 1-3 again with other starting planets.

You will then end up with several git controlled and git ignored files in this directory.

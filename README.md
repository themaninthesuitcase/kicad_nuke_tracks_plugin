# Delete Tracks KiCad Plugin

To use the handy [auto router plugin](https://github.com/random-builder/kicad_freerouting-plugin) it's really useful to start with a board clear of tracks and the zones filled. I was running the global delete tracks menu command, but thats 4 clicks this is 1.

This plugin will nuke all tracks that are not locked on the board<sup>*</sup> (you need to manually regenerate zones) so you can run the autoroute on a clean slate.

Icon by Lorc under CC BY 3.0
https://game-icons.net/1x1/lorc/mushroom-cloud.html

\* By not deleting locked tracks you can choose to keep anything you've manually routed first.
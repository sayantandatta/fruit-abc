# Fruit ABC

A tap-a-letter fruit alphabet for toddlers. Tap a letter in the ribbon and a random fruit starting with that letter pops up, with its name spoken in a British English voice and a one-line description of how it tastes. Arrows on the picture (or a swipe) move between fruits for that letter.

The fruit list comes from the [Wikijunior Fruit Alphabet](https://en.wikibooks.org/wiki/Wikijunior:Fruit_Alphabet) chart. All 99 fruits and their toddler-friendly taste sentences are in `index.html`.

## Files

- `index.html` is the whole site, with no build step. Open it in a browser or serve it from GitHub Pages.
- `images/` holds the fruit photos, named by fruit (`apple.jpg`, `dragon-fruit.jpg`). Fruits without a photo are shown as emoji or drawings.

## Adding or replacing a photo

Put a square-ish photo on a white background in `images/` and add a line to the `PHOTOS` object near the top of the script in `index.html`, for example `"Durian":"images/durian.jpg"`. The name must match the fruit name exactly.

## Photo credits

Photos are from the [Fruits-360](https://github.com/fruits-360) dataset by Mihai Oltean, licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). They were resized and converted to JPEG. 25 fruits use the dataset's original-size photos; the rest use its 100×100 photos, enlarged to 200 px.

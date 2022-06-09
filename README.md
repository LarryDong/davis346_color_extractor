# davis346_color_extractor
A demo for extracting (and drawing) color events from a DAVIS346-color.

<div align=center>
<img src="https://github.com/LarryDong/davis346_color_extractor/blob/main/about.png" width="640"  alt="demo"/><br/>
</div>

This demo includes a `.csv` file recorded from DV-software, capturing a "RGB" characters in screen with black background.

Since the color does not appear a "standard" RGB color in camera, "R" would generate green/blue events.  
Thus, an event-intensity image is show to verify the "R" generate more red events than "G" and "B".


## Usage
```bash
python extractor.py --filename=davis_color.csv --events_number=3e4
```
**Parameters**  
`@filename`: input davis346 csv file, recorded by DV-software or other drivers.  
`@events_number`: how many events to draw for each event frame


## About DAVIS346 color
Davis346-color uses a 2x2 RGBG Bayer pattern, which means 'red events' in even-row/even-col (index from 0), 'blue events' in odd-row/odd-col, 'green events' in both even-row/odd-col and odd-row/event-col.  

See [CED Dataset](https://rpg.ifi.uzh.ch/CED.html) for more details.

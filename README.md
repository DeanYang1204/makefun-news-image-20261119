[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/DeanYang1204/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/DeanYang1204/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Built for [make.fun's "Sum up 19 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261119) — $250 in USDC.

# Thursday 19 November 2026 — the day in one image

Entry for make.fun's **news-image-20261119** bounty ($250, 50 paid places).
One 1024×1024 image that sums up Thursday 19 November 2026 in four stories,
laid out as a newspaper front page: a header naming the day, a 2×2 grid of
photographic panels, and a short factual caption under each one. All type is
drawn with PIL — no generated panel carries any text, so nothing is garbled.

## The four stories (all happened / first reported on 19 November 2026)

1. **SUMMIT IN SHENZHEN — Trump, Xi and Putin meet.**
   The first-ever trilateral summit of the three leaders, in Shenzhen,
   with nuclear arms, Ukraine and Iran on the agenda.
2. **VICE CITY OPENS — GTA VI launches.**
   Rockstar's sequel arrives at midnight on PS5 and Xbox after a 13-year
   wait; critics score it 99 out of 100.
3. **CYCLONE AKVAN — Very severe storm nears India's east coast.**
   Red alerts and extremely heavy rain of 21 cm or more in Andhra Pradesh
   and Odisha; landfall expected on Friday.
4. **VOYAGER'S LIGHT-DAY — NASA confirms Voyager 1 is one light-day away.**
   16 billion miles out, the farthest any human-made object has flown;
   NASA briefs the world on the milestone today.

No other dated event is shown, and no number beyond the ones above is used.
Earlier stories (the Voyager crossing itself on Nov 18, the EU's Ukraine
loan proposal, the Alaska Senate call, the Gulf strikes of Nov 17–18) are
not presented as today's news.

## How it was made

- Four square panels generated with Gemini (web version), one per story,
  photographic/editorial style, with no text in the generated images. The
  summit panel was regenerated once: the first version had garbled writing
  on the backdrop banner, so it was remade against a plain backdrop. The
  GTA VI panel's neon signs were checked at full resolution — blank glow,
  no readable letters.
- The front page was composed from the panels with a Python/Pillow script
  (`~/workspace/makefun-news19-dev/compose.py`, kept out of this repo):
  navy header band with the date, 2×2 grid, captions drawn in DejaVu Sans.
- The finished image was read back visually: the date is prominent, all
  four stories are recognisable, captions are legible and match the facts,
  no garbled text, no fifth story.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

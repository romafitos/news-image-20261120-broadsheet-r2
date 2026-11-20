# THE WORLD LEDGER — Friday 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![Rank](https://make.fun/badge/news-image-20261120/romafitos/news-image-20261120-broadsheet-r2/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![Reward](https://make.fun/badge/news-image-20261120/romafitos/news-image-20261120-broadsheet-r2/reward.svg)](https://make.fun/bounty/news-image-20261120)

A make.fun entry for [news-image-20261120](https://make.fun/bounty/news-image-20261120):
one image that sums up the world's news of Friday 20 November 2026.

The front page is a numbered system: the date as hero — **FRIDAY 20 NOVEMBER
2026** — above 35 numbered stories across 7 regions, a numbers strip, a world
map with numbered pins, and a DATE CHECK box that names the Thursday news left
out on purpose. Lead story: Kyiv's bridges targeted in a record overnight barrage
(26 Kalibr + 72 Kh-101 + 503 drones). Every story on the page happened, or was
first reported, on Friday 20 November 2026; the fact ledger behind it is in
the build notes.

## Run

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` to the output directory (`$MAKEFUN_OUTPUT_DIR`, default
`/output`). The page itself is `frontpage.html`, rendered to `entry.png`
(1024×1024) with headless Chromium; the render is byte-identical across
runs.

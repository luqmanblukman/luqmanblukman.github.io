"""Pre-render: build the home page's experiment status from lit-review.

Reads lit-review/PROTOCOL.md (start date) and lit-review/reading-list.md
(paper statuses) and writes _generated/status.md, which index.qmd includes.
"""
import datetime as dt
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LR = ROOT / "lit-review"
OUT = ROOT / "_generated" / "status.md"
DAYS = 30
DEADLINES = [(5, "research question v1"), (14, "sprint 1 review"), (30, "sprint 2 review")]


def start_date():
    text = (LR / "PROTOCOL.md").read_text()
    m = re.search(r"\|\s*Start date[^|]*\|\s*(\d{4}-\d{2}-\d{2})", text)
    return dt.date.fromisoformat(m.group(1)) if m else None


def paper_statuses():
    rows = []
    for line in (LR / "reading-list.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and line.startswith("|") and not set(cells[0]) <= set("-: ") and cells[0] != "Paper":
            rows.append(cells[2].lower())
    return rows


def main():
    start = start_date()
    day = max(0, min(DAYS, (dt.date.today() - start).days + 1)) if start else 0
    statuses = paper_statuses()
    counts = {s: statuses.count(s) for s in ("queued", "skimmed", "deep-read")}
    upcoming = next(((d, what) for d, what in DEADLINES if d >= max(day, 1)), None)

    if not start:
        deadline = ("Not started", "")
    elif day >= DAYS:
        deadline = ("Done", "verdict written")
    else:
        deadline = (f"Day {upcoming[0]}", upcoming[1])

    pct = f"{day / DAYS * 100:.1f}%"
    filled = round(day / DAYS * 20)
    sprint = "not started" if not start else ("sprint 1 · literature" if day <= 14 else "sprint 2 · hypothesis")

    html = f"""```{{=html}}
<div class="ruled-cells">
  <div class="ruled-cell"><span class="eyebrow">Experiment</span><span class="stat">{day:02d} <span class="of">/ {DAYS} days</span></span><div class="meter"><span style="width:{pct}"></span></div></div>
  <div class="ruled-cell"><span class="eyebrow">Reading list</span><span class="stat">{len(statuses)} <span class="of">{'paper' if len(statuses) == 1 else 'papers'} · {counts['deep-read']} deep-read</span></span></div>
  <div class="ruled-cell"><span class="eyebrow">Next deadline</span><span class="stat">{deadline[0]} <span class="of">{deadline[1]}</span></span></div>
</div>
```
"""
    term = f"""```{{=html}}
<div class="term" role="img" aria-label="Experiment status: day {day} of {DAYS}">
  <div><span class="k">$</span> /exp:status</div>
  <div><span class="g">{sprint}</span></div>
  <div>day&nbsp;&nbsp;&nbsp;&nbsp;<span class="bar" style="width:{filled * 6}px"></span><span class="rest">{'░' * (20 - filled)}</span> {day:02d}/{DAYS}</div>
  <div>papers <span class="k">queued {counts['queued']} · skimmed {counts['skimmed']} · deep {counts['deep-read']}</span></div>
  <div>next&nbsp;&nbsp;&nbsp;{deadline[0].lower()}{', ' + deadline[1] if deadline[1] else ''}</div>
</div>
```
"""
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html)
    (OUT.parent / "terminal.md").write_text(term)


if __name__ == "__main__":
    main()

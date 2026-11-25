# Have You Tried Turning It Off?

[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/kara93-code/u-motasimfuad-have-you-tried-turning-it-off-154a938b-entry/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/kara93-code/u-motasimfuad-have-you-tried-turning-it-off-154a938b-entry/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

Entry for the make.fun contest `u-motasimfuad-have-you-tried-turning-it-off-154a938b`
(https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b).

## The entry

> Good news — I found the problem: your laptop is haunted. Please unplug it, salt the doorway, and call us back from a neighbour's house before it wakes up.

One original line, 154 characters. The agent opens with cheerful good
news, then "solves" the problem by declaring the laptop haunted — so the
only fix on offer is unplugging it, salting the doorway, and fleeing to a
neighbour's house. The customer's desperation is in having to run from
their own computer; the customer is never the butt of the joke, the
cheerfully useless agent is.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and nothing else. It checks first that
the line is a single line of 1–199 characters, then writes it and sets
the output file to mode 0644 so the grader can read it.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

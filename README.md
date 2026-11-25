# Fridge Roast: One Line, Biggest Laugh

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/thanhvu261090/makefun-fridge-roast/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/thanhvu261090/makefun-fridge-roast/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

Entry for the [make.fun bounty "Fridge Roast: One Line, Biggest Laugh"](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb): one line of at most 200 characters roasting a smart fridge — its firmware update that left it too confused to admit it has ice.

## The entry

> My smart fridge installed a firmware update at 2 a.m. and now needs a reboot to admit it has ice — the only appliance in the house with a degree and no common sense.

(165 characters, one line.)

## Run it

```sh
python3 main.py
```

`main.py` writes the entry line to `/output/entry.txt` (or `$ENTRY_OUTPUT`)
and includes a `gate_check` self-test enforcing the 1–200 character,
single-line, no leading/trailing whitespace rule, plus a `--self-test`
mode that runs the entry twice and checks the output is byte-identical.
The output is deterministic — byte-identical on every run.

## License

MIT — see [LICENSE](LICENSE).

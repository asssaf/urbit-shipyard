# urbit-shipyard
Ship name utilities for [Urbit](https://urbit.org)

I'm pretty new to hoon, so for now I've written this in python (maybe I'll rewrite it again in the future to run within urbit).

## Modules
### ob
Most of arvo's ob rewritten in python, provides function to convert addresses to ship names and vice versa

## Samples
### ob_cli.py
Sample CLI script that utilizes the ob library and allows finding planets by prefix/suffix. Run `ob_cli.py --help` for more info.

## Test
```
python -m unittest discover -v
```

````md
# Kattis CLI

A simple CLI tool to quickly set up Kattis problems locally.

## Install

Run the install script:

```bash
./install.sh
````

This will:

* install required dependencies
* symlink the command as `knew` into `~/.local/bin`

Make sure `~/.local/bin` is in your `PATH`.

## Usage

```bash
knew <problem-name>
```

or with a link:

```bash
knew -l <kattis-url>
```

## Example

```bash
knew parity
```

```bash
knew -l https://open.kattis.com/problems/parity
```

## What it does

* creates a directory for the problem
* adds `soln.py` (moves `<name>.py` if it exists)
* creates `README.md` with the problem link
* downloads sample inputs/outputs if available
* creates fallback `in` / `out` files when samples are unavailable

## Disclaimer

All solutions in this repository are public and free for everyone, and are intended for learning purposes only.

```
```

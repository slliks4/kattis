# Kattis CLI

> Fast local setup for Kattis problems with zero friction.

A minimal CLI tool to quickly set up Kattis problems locally.

---

## Install

Clone the repository and run:

```bash
./install.sh
```

This will:
- install required dependencies (`curl`, `unzip`)
- symlink the command as `knew` into `~/.local/bin`
- configure your shell if needed

Ensure `~/.local/bin` is in your `PATH`.

---

## Usage

```bash
knew <problem-name>
```

or with a URL:

```bash
knew -l <kattis-url>
```

---

## Examples

```bash
knew parity
```

```bash
knew -l https://open.kattis.com/problems/parity
```

---

## What it does

- creates a directory for the problem
- moves `<name>.py` → `soln.py` if it exists, otherwise creates a template
- generates a `README.md` with the problem link
- downloads sample inputs/outputs when available
- creates fallback `in` / `out` files if samples are unavailable

---

## Notes

- Problem directories are intended to be local and may be ignored via `.gitignore`
- This tool is designed for fast setup, not submission automation

---

## License

This project is licensed under the Apache License 2.0.  
See the `LICENSE` and `NOTICE` files for details.

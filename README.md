# Kattis CLI

> Fast local setup for Kattis problems with zero friction.

A minimal CLI tool to quickly set up Kattis problems locally.

---

## Install

Clone the repository and run:

```bash
./install.sh
````

This will:

* check for required dependencies (`curl`, `unzip`, `diff`)
* symlink the command as `knew` into `~/.local/bin`
* configure your shell if needed

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

## Language Support

You will be prompted to select a language:

* Python
* Java

Based on your choice:

* the correct solution file is created (`soln.py` or `soln.java`)
* a starter template is generated
* execution is configured automatically

> More languages will be added over time based on user needs.

---

## Testing

Each problem directory includes a test runner:

```bash
./test
```

This will:

* run your solution against all sample inputs (`in1`, `in2`, ...)
* compare outputs using `diff`
* display pass/fail results

---

## What it does

* creates a directory for the problem
* moves `<name>.<ext>` → `soln.<ext>` if it exists
* otherwise creates a starter template
* generates a `README.md` with the problem link
* downloads sample inputs/outputs when available
* creates fallback `in` / `out` files if samples are unavailable
* generates an executable `test` script

---

## Notes

* Problem directories are intended to be local and may be ignored via `.gitignore`
* This tool is designed for fast setup, not submission automation
* Java solutions must use:

  ```java
  public class soln
  ```

---

## License

This project is licensed under the Apache License 2.0.
See the `LICENSE` and `NOTICE` files for details.

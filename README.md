# Python Basics — Repo Guide

This repository contains short, interactive Python scripts designed for teaching absolute beginners. Each script is a self-contained, copy‑pasteable lesson that you can run in a terminal or inside VS Code. The goal: keep each example tiny, hands‑on, and suitable for a 1–5 minute classroom exercise.

---

## Recommended order (start → finish)

1. **`strings_and_methods.py`**

   * Intro to what strings are, indexing, slicing and common string methods (`.upper()`, `.split()`, `.find()`, `.replace()`), and a small user‑input challenge (leet speak).
   * Good first file: concepts are forgiving and visible immediately.

2. **`numbers_and_math.py`**

   * Integers vs floats, arithmetic, casting user input to numbers, formatting (f‑strings) and a short BMI calculator challenge.

3. **`functions_and_loops.py`**

   * How to write simple functions, `for` and `while` loops, and a small conversion exercise (F → C) demonstrating function reuse.

4. **`conditional_logic_and_control_flow.py`**

   * Comparisons, boolean logic, `if`/`elif`/`else`, `break` and `continue`, plus a factor‑finding challenge.

5. **`tuples_lists_and_dicts.py`**

   * Core data structures: tuples (immutable), lists (mutable), nested lists, and dictionaries. Includes a word frequency exercise.

6. **`oop.py`**

   * Basic class definition, methods, simple inheritance and a tiny `Counter` example — great to introduce objects as bundles of data + behavior.

7. **`file_IO.py`**

   * Read/write text files, CSV read/write using the `csv` module, and a mini high‑scores sorting example.

---



## How to run

1. Create and activate a virtual environment (recommended). You can use the built-in `venv` module **or** Conda (Anaconda / Miniconda). Pick whichever fits your workflow.

* **Using `venv` (built-in, cross-platform)**

  * **Windows (PowerShell)**

  ```powershell
  py -3 -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

  * **macOS / Linux (bash/zsh)**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

  * To deactivate a venv:

  ```bash
  deactivate
  ```

* **Using Conda (Anaconda or Miniconda) — alternative**

  Conda is a popular choice for managing environments and packages, especially in teaching and data‑science contexts.

  * **Create a new environment (example name `pybasics`) with a specific Python version:**

  ```bash
  conda create -n pybasics python=3.11 -y
  ```

  * **Activate the environment:**

  ```bash
  conda activate pybasics
  ```

  * **Install packages using conda (recommended) or pip if needed:**

  ```bash
  conda install numpy pandas         # example with conda
  pip install -r requirements.txt    # pip inside the conda env if you need packages from PyPI
  ```

  * **Use the Anaconda Prompt on Windows** for the smoothest experience, or run `conda init powershell` once and restart PowerShell to enable `conda activate` there.

  * **Create an environment from an environment.yml file:**

  ```bash
  conda env create -f environment.yml
  ```

  * **Export an environment to share with others:**

  ```bash
  conda env export > environment.yml
  ```

  * **Remove the environment when you're done:**

  ```bash
  conda remove -n pybasics --all
  ```

2. Run any script from the repo root:

```bash
python strings_and_methods.py
```

Each script is interactive (uses `input()`), so run them in a terminal or VS Code integrated terminal rather than double‑clicking.


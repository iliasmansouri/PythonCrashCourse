# README — Getting Your Environment Ready

A friendly, beginner-oriented guide to preparing a development environment for Python projects. This README walks you through installing an IDE, Anaconda, Git and Docker, and explains in plain language why each tool is useful.

---

## Table of contents

- [README — Getting Your Environment Ready](#readme--getting-your-environment-ready)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Step 1 - Pick an IDE / Code Editor](#step-1---pick-an-ide--code-editor)
  - [Step 2 - Install Anaconda (recommended for beginners)](#step-2---install-anaconda-recommended-for-beginners)
  - [Step 3 - Install Git](#step-3---install-git)
  - [Step 4 - Install Docker (optional but powerful)](#step-4---install-docker-optional-but-powerful)
  - [Quick checklist](#quick-checklist)
  - [Short glossary (plain language)](#short-glossary-plain-language)

---

## Introduction

This repository contains scripts that require a basic Python development environment. This README helps beginners get set up with tools that make development easier, reproducible, and collaborative.

If you're new to programming, don't worry — follow the steps in order and copy the commands into your terminal.

---

## Prerequisites

* A computer with internet access (Windows, macOS, or Linux).
* Basic comfort using a terminal / command prompt is helpful but not required.

---

## Step 1 - Pick an IDE / Code Editor

An **IDE** (Integrated Development Environment) or code editor is where you write and run your code. Think of it as a specialized text editor with useful extras for coding.

Beginner-friendly options:

* **VS Code** — Lightweight, cross-platform, and highly recommended.
* **PyCharm Community** — Excellent Python support and debugging tools.
* **Thonny** — Extremely beginner-friendly; tailored for teaching Python.
* **Jupyter Notebook / JupyterLab** — Interactive environment popular in data science.

👉 If you’re unsure, start with **VS Code**.

---

## Step 2 - Install Anaconda (recommended for beginners)

**What is Anaconda?**

Anaconda bundles Python with many popular packages (NumPy, pandas, matplotlib, Jupyter, and more) and includes `conda`, a tool for managing packages and isolated environments.

**Why use Anaconda?**

* Install Python and commonly used packages with minimal fuss.
* Create isolated environments per project so dependencies don’t conflict.
* Run Jupyter notebooks and JupyterLab easily.

**Download & install (quick):**

1. Visit the Anaconda download page and choose the installer for your OS.
2. Run the installer and follow prompts. On Windows you can use Anaconda Prompt or allow conda on PATH.
3. Verify installation:

```bash
conda --version
```

4. Create and activate an environment (example):

```bash
conda create -n myenv python=3.11
conda activate myenv
conda install jupyterlab numpy pandas
```

5. Launch JupyterLab:

```bash
jupyter lab
```

**Tip:** Use `conda create` / `conda activate` to keep each project’s libraries isolated.

---

## Step 3 - Install Git

**What is Git?**

Git is a version control system. It tracks changes to files over time so you can revert, branch, and collaborate safely.

**Why use Git?**

* Save snapshots of your project (commits).
* Revert to older versions if something breaks.
* Collaborate and share via platforms like GitHub or GitLab.

**Download & install (quick):**

1. Download Git from [https://git-scm.com/](https://git-scm.com/) or install via your OS package manager.
2. Verify:

```bash
git --version
```

3. Configure your identity (first time only):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

4. Basic workflow (clone, edit, commit, push):

```bash
git clone https://github.com/username/repo.git
cd repo
# edit files
git add .
git commit -m "Describe what I changed"
git push origin main
```

**Tip:** Commit frequently with clear messages; use branches to isolate features.

---

## Step 4 - Install Docker (optional but powerful)

**What is Docker?**

Docker packages your application and everything it needs (Python version, libraries, system packages) into a **container**. That container runs the same way on any machine with Docker installed.

**Why use Docker?**

* Ensures reproducible environments: "it works on my machine" becomes less of a problem.
* Simplifies deployment of apps (web APIs, services).
* Useful when sharing projects with teammates or deploying to servers.

**When to start using it:**

Docker is optional for small beginner projects. Learn it after you’re comfortable with Python and Git.

**Download & install (quick):**

1. Install **Docker Desktop** (Windows/macOS) or Docker Engine (Linux).
2. Verify:

```bash
docker --version
```

3. Quick example — run an interactive Python container:

```bash
docker run --rm -it python:3.11 bash
# inside container: python
```

4. Example Dockerfile for a small Python app (place in project root):

```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Build and run the image:

```bash
docker build -t myapp .
docker run -p 5000:5000 myapp
```

**Tip:** Start by running official Python images (`docker run python`) to experiment before dockerizing a whole project.

---

## Quick checklist

* [ ] IDE installed (e.g., VS Code)
* [ ] Anaconda installed (`conda --version`)
* [ ] Git installed & configured (`git --version` and `git config --global ...`)
* [ ] Docker installed if needed (`docker --version`)

---

## Short glossary (plain language)

* **IDE / Code editor** — where you write and run your code (like a word processor for code).
* **Anaconda / conda** — a distribution that packages Python, common libraries, and an environment manager (useful for data science and dependency management).
* **Git** — a tool that tracks changes to files and helps you collaborate and manage history.
* **Docker** — packages your app and its environment so it runs consistently anywhere.

---


*Happy coding!* 🚀

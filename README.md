# Build an RPG Character

A clean, lightweight Python script designed to evaluate and display custom RPG character stats based on user-defined points and formatting rules.

## 🚀 How It Works

The script systematically evaluates character creation logic using multiple conditional validation checks and outputs a styled stat sheet:

* **Name Validation:** Ensures the character name is a valid string, is not empty, does not exceed 10 characters, and contains no spaces.
* **Type & Range Check:** Verifies that all allocated stats (Strength, Intelligence, and Charisma) are integers ranging strictly between 1 and 4.
* **Point Budget Check:** Enforces a strict starting rule where the total sum of all three attributes must equal exactly 7 points.
* **Visual Rendering:** Dynamically generates and prints a progress-bar style stat sheet using custom dot indicators (`●` and `○`).

## 🛠️ Variables Evaluated

| Variable | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | The unique identifier for the RPG character. |
| `strength` | `int` | The physical power stat (validated between 1 and 4). |
| `intelligence` | `int` | The mental acuity stat (validated between 1 and 4). |
| `charisma` | `int` | The social influence stat (validated between 1 and 4). |
## 💻 Tech Stack
* **Language:** Python 3.x
* **Concepts:** Input validation, conditional control structures (`if`), string manipulation, and loop-based UI rendering.

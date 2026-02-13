from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
import json
import pyparsing as p
import os
import shutil

# ==========================================
# Helpers
# ==========================================

def create_config():
    return {
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def is_database(dir: Path):
    return (dir / "database.json").exists()

@dataclass
class State:
    path: Path

# ==========================================
# Expressions
# ==========================================

def evaluate_arithmetic(tokens):
    return eval("".join(map(str, tokens)))

def evaluate_values(tokens):
    result = []
    for token in tokens:
        if token in ["(", ")", "VALUES"]: continue
        result.append(token)
    return [result]

# ==========================================
# Statements
# ==========================================

# =======
# For tables and databases
# =======

def evaluate_create(tokens):
    _, command, dir = tokens
    dir = Path(dir)
    if (command == "DATABASE"):
        config = create_config()
        if dir.exists():
            return "A file or directory with the same name already exists."
        dir.mkdir()
        with (dir / "database.json").open("w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        return f"Database {str(dir)} successfully created."
        
def evaluate_drop(tokens):
    _, command, dir = tokens
    dir = Path(dir)
    if (command == "DATABASE"):
        if not dir.exists():
            return "Directory does not exist."
        if not is_database(dir):
            return "Directory is not a database."
        shutil.rmtree(dir)
        return f"Database {str(dir)} successfully deleted."

def evaluate_show(tokens):
    _, command = tokens
    working_dir = Path(".")
    if (command == "DATABASES"):
        result = ""
        for dir in working_dir.iterdir():
            if is_database(dir):
                result += str(dir) + " "
        if result == "": return "No databases in the current directory."
        return result

# =======
# Utility
# =======

def evaluate_print(tokens):
    return tokens[1]

def evaluate_use(tokens):
    _, database = tokens
    selected = Path(database)
    if not is_database(selected):
        return "The specified database does not exist."
    State.path = selected
    return f"Database {database} successfully selected."

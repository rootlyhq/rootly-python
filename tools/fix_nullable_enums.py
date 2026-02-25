#!/usr/bin/env python3
"""
Post-generation fix for nullable enum properties.

openapi-python-client doesn't handle `nullable: true` on enum properties,
only `null` in enum values. This script patches the generated check functions
to pass through None values.

Run after: make regenerate
Usage: python tools/fix_nullable_enums.py

See: https://github.com/openapi-generators/openapi-python-client/issues/1405
"""

import re
from pathlib import Path


def fix_check_function(content: str) -> str | None:
    """
    Patch enum check functions to handle None.

    Handles both single-line and multi-line function signatures.
    """
    # Skip if already patched
    if "if value is None:\n        return None" in content:
        return None

    # Pattern for single-line: def check_foo(value: str) -> FooType:
    single_line_pattern = r"(def check_\w+\()(value: str)(\) -> )(\w+)(:)"

    # Pattern for multi-line:
    # def check_foo(
    #     value: str,
    # ) -> FooType:
    multi_line_param_pattern = r"(    value: str)(,?\n)"
    multi_line_return_pattern = r"(\) -> )(\w+)(:)"

    modified = False

    # Check which pattern matches
    if re.search(single_line_pattern, content):
        # Single line function
        content = re.sub(single_line_pattern, r"\1value: str | None\3\4 | None\5", content)
        modified = True
    elif re.search(multi_line_param_pattern, content):
        # Multi-line function
        content = re.sub(multi_line_param_pattern, r"    value: str | None\2", content)
        content = re.sub(multi_line_return_pattern, r"\1\2 | None\3", content)
        modified = True

    if not modified:
        return None

    # Now add the None check after the function definition
    # Find "if value in " and add None check before it
    lines = content.split("\n")
    new_lines = []

    for i, line in enumerate(lines):
        # Look for the first "if value in" after a check function
        if "    if value in " in line:
            # Check if previous non-empty line is the function signature end or another statement
            # Add the None check
            new_lines.append("    if value is None:")
            new_lines.append("        return None")
        new_lines.append(line)

    return "\n".join(new_lines)


def process_file(filepath: Path) -> bool:
    """Process a single file. Returns True if modified."""
    content = filepath.read_text()

    # Only process files with check_ functions that have "if value in"
    if "def check_" not in content or "if value in " not in content:
        return False

    fixed = fix_check_function(content)

    if fixed:
        filepath.write_text(fixed)
        return True

    return False


def main():
    models_dir = Path("rootly_sdk/models")

    if not models_dir.exists():
        print(f"Error: {models_dir} not found")
        return 1

    fixed_count = 0
    for filepath in sorted(models_dir.glob("*.py")):
        if process_file(filepath):
            print(f"Fixed: {filepath.name}")
            fixed_count += 1

    print(f"\nPatched {fixed_count} files")
    return 0


if __name__ == "__main__":
    exit(main())

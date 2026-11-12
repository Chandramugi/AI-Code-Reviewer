
import ast
import subprocess
import sys


def check_syntax(code):
    """Check Python syntax using AST."""

    try:
        ast.parse(code)
        return {
            "valid": True,
            "message": "No syntax errors found."
        }

    except SyntaxError as error:
        return {
            "valid": False,
            "message": str(error),
            "line": error.lineno
        }


def analyze_structure(code):
    """Analyze basic Python code structure."""

    try:
        tree = ast.parse(code)

        functions = [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]

        classes = [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
        ]

        imports = [
            node.names[0].name
            for node in ast.walk(tree)
            if isinstance(node, ast.Import) and node.names
        ]

        return {
            "functions": functions,
            "classes": classes,
            "imports": imports,
            "lines": len(code.splitlines())
        }

    except SyntaxError:
        return {}



def analyze_quality(code):
    """Run Pylint on Python source code."""

    try:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pylint",
                "--from-stdin",
                "reviewed_code.py"
            ],
            input=code,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30
        )

        return result.stdout + result.stderr

    except subprocess.TimeoutExpired:
        return "Pylint analysis timed out."

    except Exception as error:
        return f"Analysis error: {error}"




def run_static_analysis(code):
    """
    Execute complete static analysis
    and extract the Pylint score.
    """

    syntax_result = check_syntax(code)

    if not syntax_result["valid"]:
        return {
            "syntax": syntax_result,
            "structure": {},
            "quality": "Skipped due to syntax errors.",
            "pylint_score": None
        }

    structure_result = analyze_structure(code)

    quality_result = analyze_quality(code)

    pylint_score = extract_pylint_score(
        quality_result
    )

    return {
        "syntax": syntax_result,
        "structure": structure_result,
        "quality": quality_result,
        "pylint_score": pylint_score
    }


import re


def extract_pylint_score(pylint_output):
    """
    Extract the Pylint score from its output.
    """

    match = re.search(
        r"rated at ([\d.]+)/10",
        pylint_output
    )

    if match:
        return float(match.group(1))

    return None


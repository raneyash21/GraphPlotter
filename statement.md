# Project: Student Function Plotter

## Problem Statement
Many students learning algebra, trigonometry and calculus struggle to visualise mathematical functions quickly and interactively. Existing graphing tools can be feature‑heavy or require learning a specific input format. Students need a simple, safe, and immediate way to type a function (like a search box) and see its graph so they can build intuition about polynomials, trigonometric functions and other expressions.

## Goal
Build a lightweight desktop application that lets students type a single mathematical expression using variable `x` and instantly plot the function over a configurable domain. The UI must be extremely simple (one input bar like a search field), suitable for classroom and self-study use.

## Objectives
- Provide a single-line input where users type an expression (examples: `sin(x)`, `x**2`, `sin(x)+0.5*x**2`, `exp(-x**2)`).
- Plot the typed expression over a user-specified domain (x start, x end, number of points).
- Offer quick example expressions and simple controls (Plot, Clear).
- Evaluate expressions safely with a restricted namespace (only math/NumPy functions allowed).
- Be cross-platform (Windows/Mac/Linux) using standard Python libraries (Tkinter, matplotlib, NumPy).

## Scope
In scope:
- Single-expression input and plotting.
- Domain controls and basic validation.
- A short list of allowed functions (sin, cos, tan, exp, log, sqrt, abs, pi, e, and NumPy via `np`).
- Simple example chooser and error messages for invalid inputs.

Out of scope (can be added later):
- Multiple simultaneous plots/overlays.
- Symbolic manipulation or calculus operations.
- Exporting graphs/data (optional extension).
- User accounts or remote services.

## Functional Requirements
1. Single-entry input bar for expressions using `x`.
2. Plot action (button or Enter key) to render the function curve.
3. Domain controls: x start, x end, number of sample points.
4. Quick examples selector to populate the input bar.
5. Clear/close plots control.
6. Input validation and user-friendly error messages when expression evaluation fails or domain parameters are invalid.

## Non-Functional Requirements
- Usability: Very low learning curve — single input bar as primary interaction.
- Performance: Plot generation for typical settings (<= 5000 points) should be near-instant on modern student laptops.
- Security: Restrict evaluation environment to prevent arbitrary code execution; only expose safe math/NumPy functions.
- Reliability: Graceful handling of invalid input, numeric errors (NaN/Inf), and mismatched output shapes.
- Portability: Runs with standard Python and common packages (NumPy, matplotlib, Tkinter).
- Maintainability: Small, well-documented codebase with clear separation between UI, parsing/evaluation, and plotting.

## Success Criteria
- A student can type an expression in one input bar, press Enter (or click Plot), and see a correct graph for typical polynomials and trig functions.
- The app rejects unsafe expressions and shows meaningful error messages.
- Example expressions work out-of-the-box and help students get started immediately.

## Deliverables
- Source code (single-file Tkinter app or small module) with comments.
- README with setup and usage instructions.
- statement.md (this file) and a short demo or screenshots.
- Optional: unit tests for expression parsing/evaluation and domain validation.

## Constraints & Assumptions
- Users will provide numeric domain bounds (start, end) and a positive integer for points.
- The tool is educational; not intended to run untrusted code from unknown sources.
- Python environment has NumPy and matplotlib installed.

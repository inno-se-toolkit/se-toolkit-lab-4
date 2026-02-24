# Testing

<h2>Table of contents</h2>

- [What is testing](#what-is-testing)
- [Assertion](#assertion)

<!-- TODO explain types of analysis - dynamic and static -->

## What is testing

Testing is the practice of verifying that software behaves as expected by running it with specific inputs and checking that the outputs match the expected results.

This is a form of dynamic analysis — the code is actually executed, as opposed to static analysis which inspects code without running it.

Tests catch bugs early, prevent regressions when code changes, and document the intended behavior of a program.

Examples:

- [Testing in `Python`](./python.md#testing)

## Assertion

An assertion is a statement that checks whether a given condition is true. If the condition is false, the assertion fails and raises an error, stopping the test immediately. Assertions are the primary mechanism for verifying expected behavior in tests — each test typically ends with one or more assertions that confirm the code produced the right result.

Examples:

- [The `assert` statement in `Python`](./python.md#the-assert-statement)

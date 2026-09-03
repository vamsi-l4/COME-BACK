# Day 9 - Sets and Membership Logic

## Goal

Learn when a problem only requires remembering whether a value exists.

## Topics

- Set
- Unique values
- Membership checking
- Seen tracking
- Duplicate detection
- Intersection
- Union
- Set vs Dictionary

## Problems

1. Contains Duplicate
2. Remove Duplicates
3. Intersection of Two Arrays
4. Union of Two Arrays
5. Missing Number using Set
6. First Repeated Character

## Main Patterns

### Seen Tracking

Remember values that already appeared.

### Membership

Ask:

Does this value exist?

### Unique Values

Use a set when duplicates are not needed.

## Set vs Dictionary

Set:
item exists or not

Dictionary:
item → additional information

Examples:

Set:
Have I seen 5?

Dictionary:
5 → count
5 → index

## Problem Solving Process

1. Understand the problem
2. Identify input
3. Identify output
4. Take a small example
5. Observe what changes
6. Ask what information must be remembered
7. Decide Set / Dictionary / other pattern
8. Choose variables
9. Explain approach
10. Dry run
11. Write code
12. Test edge cases
13. Debug

## Main Learning

If I only need to know whether a value appeared before,
I should think about a Set.
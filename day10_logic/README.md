# Day 11 - Sliding Window

## Goal

Learn how to maintain a changing contiguous range instead of repeatedly recalculating the same elements.

## Topics

- Sliding Window
- Fixed-size Window
- Variable-size Window
- Expand Window
- Shrink Window
- Contiguous Subarray
- Substring
- Set + Sliding Window
- Two Pointers + Sliding Window

## Problems

1. Maximum Sum Subarray of Size K
2. Maximum Average Subarray
3. Minimum Size Subarray Sum
4. Longest Substring Without Repeating Characters
5. Maximum Sum Subarray

## Fixed Window

Window size is known.

Example:

Find maximum sum of K consecutive elements.

Pattern:

Add incoming element.
Remove outgoing element.
Update answer.

## Variable Window

Window size changes.

Right pointer expands the window.

Left pointer shrinks the window.

General pattern:

Expand until condition becomes valid.

Then shrink while possible.

Update the answer.

## Important Questions

- Is the range contiguous?
- Is the window size fixed?
- What makes the window valid?
- What makes it invalid?
- When should right move?
- When should left move?
- What information must be maintained?

## Main Learning

Do not recalculate information that can be maintained while the window moves.
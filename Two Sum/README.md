# LeetCode Solutions

My solutions to LeetCode problems, with explanations for practice.

## Problems

### 1. Two Sum

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.

**File:** [`two_sum.py`](two_sum.py)

---

#### Approach 1: Brute Force

Check every possible pair of numbers to see if any two add up to the target.

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

**How it works:**
- Loop through each number (`i`)
- For each one, loop through every number *after* it (`j`)
- Check if the pair adds up to the target
- If it does, return their indices

**Time complexity:** O(n²) — for every number, we check almost every other number again, so it gets slow as the list grows.

**Space complexity:** O(1) — no extra storage used.

---

#### Approach 2: Hash Map (Optimal)

Use a dictionary to remember numbers we've already seen, so we only need to loop through the list once.

```python
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```

**How it works:**
- `seen` is a dictionary storing `{number: index}` for numbers we've already passed
- For each number, calculate its `complement` (the value needed to reach the target)
- Check if that complement is already in `seen`
  - If yes → we found the pair, return both indices
  - If no → store the current number and move on
- Because dictionary lookups are close to instant, we avoid re-scanning the list

**Time complexity:** O(n) — we only loop through the list once.

**Space complexity:** O(n) — in the worst case, we store almost every number in the dictionary.

---

#### Comparison

| Approach    | Time  | Space | Notes                          |
|-------------|-------|-------|--------------------------------|
| Brute Force | O(n²) | O(1)  | Simple, but slow on large lists |
| Hash Map    | O(n)  | O(n)  | Faster, trades memory for speed |

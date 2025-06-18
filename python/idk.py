arrays = [list(map(int, input().split())) for _ in range(5)]

# Calculate row sums
row_sums = [sum(row) for row in arrays]

# Calculate column sums
col_sums = [sum(arrays[row][col] for row in range(5)) for col in range(5)]

# Find the row with odd sum
odd_row = next((i for i, r_sum in enumerate(row_sums) if r_sum % 2 != 0), -1)

# Find the column with odd sum
odd_col = next((j for j, c_sum in enumerate(col_sums) if c_sum % 2 != 0), -1)

# Print result
print(f"{odd_row} {odd_col}")


grades = [85, 90, 78, 92, 88]
avg_grade = sum(grades) / len(grades)
ht_grade = max(grades)
lt_grade = min(grades)
ab_avg = [grade for grade in grades if grade > avg_grade]
print(f"Average Grade: {avg_grade:.2f}")
print(f"Highest Grade: {ht_grade}")
print(f"Lowest Grade: {lt_grade}")
print(f"Above Average: {ab_average}")
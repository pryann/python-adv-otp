# x = 10
# print(x)

print(x := 3)

yearly_salaries = [50_000, 60_000, 70_000, 80_000]

# A version
yearly_salaries_statistics = {
    "count": len(yearly_salaries),
    "summa": sum(yearly_salaries),
    "average": sum(yearly_salaries) / len(yearly_salaries),
}

# B version
count_yearly_salaries = len(yearly_salaries)
summa_yearly_salaries = sum(yearly_salaries)

yearly_salaries_statistics = {
    "count": count_yearly_salaries,
    "summa": summa_yearly_salaries,
    "average": summa_yearly_salaries / count_yearly_salaries,
}

# C version
yearly_salaries_statistics = {
    "count": (count_yearly_salaries := len(yearly_salaries)),
    "summa": (summa_yearly_salaries := sum(yearly_salaries)),
    "average": summa_yearly_salaries / count_yearly_salaries,
}

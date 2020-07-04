选出所有 bonus < 1000 的员工的 name 及其 bonus。

Employee 表单

+-------+--------+-----------+--------+
| empId |  name  | supervisor| salary |
+-------+--------+-----------+--------+
|   1   | John   |  3        | 1000   |
|   2   | Dan    |  3        | 2000   |
|   3   | Brad   |  null     | 4000   |
|   4   | Thomas |  3        | 4000   |
+-------+--------+-----------+--------+
empId 是这张表单的主关键字
Bonus 表单

+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
empId 是这张表单的主关键字
输出示例：
+-------+-------+
| name  | bonus |
+-------+-------+
| John  | null  |
| Dan   | 500   |
| Brad  | null  |
+-------+-------+

# Write your MySQL query statement below

select
    name, bonus
from
    employee as e left join bonus as b on e.empid = b.empid

# 这里要是只有一个bonus, 会默认去掉null
# 所以我们要加一个bonus is null
where bonus is null or bonus < 1000

# https://leetcode-cn.com/problems/employee-bonus/solution/yuan-gong-jiang-jin-by-leetcode-solution/
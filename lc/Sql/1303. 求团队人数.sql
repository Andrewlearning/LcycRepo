员工表：Employee

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| team_id       | int     |
+---------------+---------+
employee_id 字段是这张表的主键，表中的每一行都包含每个员工的 ID 和他们所属的团队。
编写一个 SQL 查询，以求得每个员工所在团队的总人数。

查询结果中的顺序无特定要求。

查询结果格式示例如下：

Employee Table:
+-------------+------------+
| employee_id | team_id    |
+-------------+------------+
|     1       |     8      |
|     2       |     8      |
|     3       |     8      |
|     4       |     7      |
|     5       |     9      |
|     6       |     9      |
+-------------+------------+
Result table:
+-------------+------------+
| employee_id | team_size  |
+-------------+------------+
|     1       |     3      |
|     2       |     3      |
|     3       |     3      |
|     4       |     1      |
|     5       |     2      |
|     6       |     2      |
+-------------+------------+
ID 为 1、2、3 的员工是 team_id 为 8 的团队的成员，
ID 为 4 的员工是 team_id 为 7 的团队的成员，
ID 为 5、6 的员工是 team_id 为 9 的团队的成员。


# Write your MySQL query statement below

select
    e.employee_id, c.team_size
from
    employee e,
    -- 我们在这里求出， 每个team_id对应的size是多少
    -- 因为count(*) 不代表任何colume，所以我们要 as team_size来给这一列命名
    (select team_id,count(*) as team_size from employee e group by team_id ) as c
where
    -- 最后选出两个表一样的team id
    c.team_id = e.team_id


-- 链接：https://leetcode-cn.com/problems/find-the-team-size/solution/dui-xiao-bai-you-hao-fen-jie-tu-xiang-xi-jiang-jie/

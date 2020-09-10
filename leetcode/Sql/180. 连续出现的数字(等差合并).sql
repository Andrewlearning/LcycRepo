--编写一个 SQL 查询，查找所有至少连续出现三次的数字。
--
--+----+-----+
--| Id | Num |
--+----+-----+
--| 1  |  1  |
--| 2  |  1  |
--| 3  |  1  |
--| 4  |  2  |
--| 5  |  1  |
--| 6  |  2  |
--| 7  |  2  |
--+----+-----+
--例如，给定上面的 Logs 表， 1 是唯一连续出现至少三次的数字。
--
--+-----------------+
--| ConsecutiveNums |
--+-----------------+
--| 1               |

-- 因为可能有同一个数字，可能能构成多个等差，但我们只要一个就好了
SELECT DISTINCT
    l1.Num AS ConsecutiveNums

-- 这等于把三个表同时合并到了一起
FROM
    Logs l1,
    Logs l2,
    Logs l3

--满足等差顺序且相等
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;

-- 作者：LeetCode
-- 链接：https://leetcode-cn.com/problems/consecutive-numbers/solution/lian-xu-chu-xian-de-shu-zi-by-leetcode/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
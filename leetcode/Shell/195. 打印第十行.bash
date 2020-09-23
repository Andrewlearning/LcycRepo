打印第十行
sed -n '10p' file.txt

打印一到十行
sed -n '1,10p' file.txt

查找指定字符
grep -n 'KeyWord' file.txt

打印指定字符上下5行
grep -C 5 'KeyWord' file.txt

打印指定字符上下N行
grep -A 100 -B 100 'KeyWord' file.txt
-A after 后面
-B before 前面

查找指定字符出现次数
grep -o 'KeyWord' file.txt | wc -l

#作者：FlagMain
#链接：https://leetcode-cn.com/problems/tenth-line/solution/da-yin-di-shi-xing-cha-zhao-chang-yong-ming-ling-b/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
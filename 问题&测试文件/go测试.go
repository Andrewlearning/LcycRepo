package main

import (
	"fmt"
	"strconv"
)

func main() {
	//test1()
	test2()
}


func test1() {
	println(1 == 1)

	//stack := []int{9,9,9,9,9}
	//
	//for i, val := range stack {
	//	println(i, val)
	//}

	ss := "aaa"
	hashmap := map[byte]byte{}

	for i := range ss {
		x := ss[i]
		hashmap[x] = x
	}
}

func test2() {

	hashmap := map[string]string {
		"2" : "abc",
	}

	for i := 3; i < 10; i++ {
		curKey := strconv.Itoa(i)
		//var curValue string
		runeCurKey := []rune(curKey) - 1
		preKey := string(runeCurKey)

		for j, value  := range hashmap[preKey] {
			fmt.Println(j)
			fmt.Println(value)
		}

	}


	fmt.Println(string('A'+ 32))
	fmt.Println('a')
	ru := 'a' + 1
	fmt.Println(string(ru))

}


// 一个很好的教学模板
func groupAnagrams(strs []string) [][]string {

	hashmap := map[[26]int][]string{}

	// 不用的index变量，就用_表示，因为不用的话会报错
	for _, str := range strs {
		cnt := [26]int{}
		for _, char := range str {
			// 这里ord相减，只能使用单引号
			cnt[char - 'a'] ++
		}

		hashmap[cnt] = append(hashmap[cnt], str)
	}

	res := [][]string{}
	for _, val := range hashmap {
		res = append(res, val)
	}

	return res

}
package main

func main() {
	test1()
}

func test1() {

	var stack = []int{}

	for i := 0; i < 10; i++ {
		println(stack == nil)
		stack = append(stack, i)
		println(stack)
	}

}
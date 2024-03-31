"""
相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：

线程 A 将调用 zero()，它只输出 0 。
线程 B 将调用 even()，它只输出偶数。
线程 C 将调用 odd()，它只输出奇数。
每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n。

输入：n = 2
输出："0102"
说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"

"""

class ZeroEvenOdd {
    private int n;
    private boolean zeroFlag; // 判断是否可打印zero，为true时可
    private boolean evenFlag; // 判断是否可打印even，为true时可打印
    private boolean oddFlag; // 判断是否可打印odd，为true时可打印
    private boolean flag;   // true可打印odd, false可打印even
    private static Object lock = new Object();

    public ZeroEvenOdd(int n) {
        this.n = n;
        this.flag = true;
        this.zeroFlag = true;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            synchronized (lock) {
                while (!zeroFlag) {
                    lock.wait();
                }
                printNumber.accept(0);
                if(flag){ // 可打印odd
                    oddFlag = true;
                }else{
                    evenFlag = true;
                }
                zeroFlag = false;
                lock.notifyAll();
            }

        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            synchronized (lock) {
                while (!evenFlag) { // evenFlag为false时，锁等待
                    lock.wait();
                }
                printNumber.accept(i);
                zeroFlag = true;
                evenFlag = false;
                flag = true;//下一次打印odd
                lock.notifyAll();

            }

        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            synchronized (lock) {
                while (!oddFlag) { // oddFlag为false时，锁等待
                    lock.wait();
                }
                printNumber.accept(i);
                zeroFlag = true;
                oddFlag = false;
                flag = false;//下一次打印even
                lock.notifyAll();
            }

        }
    }
}
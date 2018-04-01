'''杨辉三角定义如下：
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：'''
def triangle():
    L = [1];
    while True:
        yield L;
        LC = L + [0];
        L = [LC[i-1] + LC[i] for i in range(len(LC))];
# The basic knowledge of C++

## new and delete

用于堆上分配和释放内存，与C中`malloc`和`free`相似。

```cpp
int* pt=new int;
int* pt1=new int[10];
delete pt;
delete[] pt1;

MyClass* obj = new MyClass;  // 调用构造函数(constructor)
delete obj;                  // 调用析构函数(destructor)并释放内存
```

## Reference

reference(引用)本质是个变量的别名，引用允许我们通过别名访问变量，而不需要复制其值。`type &ref = variable`。
特点：

- 引用在声明时就必须初始化且之后不能改变引用的对象。
- 引用本质上是一个别名，它和原始对象共享同一内存地址。
- 引用用于函数参数传递时，避免了大对象的复制，并且可以在函数内部修改外部对象的值。

用法：

```cpp
void increment(int &x) {
    x++;  // 通过引用修改外部变量的值
}


int& getMax(int &a, int &b) {
    return (a > b) ? a : b;  // 返回引用
}
int x=10,y=20;
getMax(x,y)=30;  //现在y=30


void printValue(const int &x) {//传递大型对象/结构体时尤其重要，可以避免不必要的复制，同时保护原始数据。
    std::cout << x << std::endl;  // 不能修改 x
}
int x;
printValue(x);
```

**与指针的区别**：

| 特性                   | 引用（Reference）                          | 指针（Pointer）                             |
|------------------------|-----------------------------------------|-------------------------------------------|
| **语法**               | `type &ref = variable;`                  | `type* ptr = &variable;`                   |
| **是否可为空**         | 不可为空（必须引用有效的对象）            | 可以为空（指向 `nullptr`）                  |
| **是否可以修改指向对象** | 不可以修改引用指向的对象                  | 可以通过修改指针来改变它指向的对象        |
| **内存开销**           | 引用没有额外的内存开销，它是一个别名      | 指针有额外的内存开销（存储指针本身的地址）  |
| **使用场景**           | 更常用于函数参数传递、返回引用等          | 更灵活，可以指向不同的对象，但需要管理内存 |
| **常量引用**           | `const type &`                           | `const type*`                              |

限制：

- No pointers to reference: `int& * p;//illegal;`
- No array of references

## const

C++中关键字，用于声明常量或常量表达式，表示数据不可修改。const 是在程序运行时确定的常量，编译器在编译时无法确定其值。

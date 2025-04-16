# 结构体（struct）

C++中的结构体和类很像，结构体中如果没有范围限定符，默认为`pubilc`，类中默认为`private`。

结构体中可以定义函数，但是C不行，C的结构体只能包含数据成员。C、C++结构体都可以嵌套。

结构体也可以有构造函数：


```cpp
struct MyStruct {
    int x;
    int y;
    // 构造函数
    MyStruct(int a, int b) : x(a), y(b) {}
    // 成员函数，直接访问成员变量并输出
    void display() {
        cout << "x = " << x << ", y = " << y << endl;
    }
};
int main() {
    MyStruct obj(5, 10);  // 创建结构体对象并调用构造函数
    obj.display();         // 调用结构体的成员函数
}
```

声明为静态的变量和函数可在结构体外使用范围分解运算符`::`来访问。
静态成员变量和函数是属于整个结构体/类的，而不是结构体/类的某个实例，所以即使结构体/类的静态成员被声明为 `private`，也可以在定义外访问。

```cpp
struct MyStruct {
private:
static bool is_struct;

public:
    static int x;  // 静态数据成员
    static void showX() {  // 静态成员函数
        cout << "x = " << x << endl;
    }
};

Mystruct::is_struct=false;
Mystruct::x=10;
Mystruct::showX();
```


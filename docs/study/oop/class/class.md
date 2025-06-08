# Class

## 访问权限

- **private**: 只可在类内使用，被继承也不能使用
- **protected**: 继承的子类可以使用，但是类外不可使用
- **public**: 类内外都可使用

类内如果不说明访问权限，默认是`private`的。

私有成员的限制是类级别的，而不是对象级别的，所以类的成员函数可以访问同类任何对象的私有成员或函数。如下面拷贝构造函数

```cpp
class Integer{
    int val;
public:
    Integer():val(0){}
    Integer(const Integer& other): val(other.val){}
};
```

## 静态成员变量与函数

- `static`修饰的变量与函数是属于**类本身**的，可以不实例化类直接使用`Class::`来访问，即使修饰的变量和函数是`private`的。

- 静态成员变量的值需要在类加载时初始化，并且它们在所有**对象实例之间共享**。**必须在类外部定义其值**，如果在内部（比如声明时或构造函数中）定义值，当实例化多个对象时就会导致静态成员变量重复定义错误。

- 静态成员函数没有 `this` 指针，因为静态成员函数不依赖于具体的对象，所以静态成员函数也不能访问类内的非静态成员变量（因为它们随具体对象变化）。

```cpp title="static member"
class Room{
  static int door=1;
  static void openDoor(){cout<<"Door was opened.\n";}
};
cout<<Room::door;
Room::openDoor();
```

## this 指针

- this 指针 是一个**隐式参数**，它存在于每个**非静态**成员函数的内部。this 指针指向当前对象的地址，即它指向调用该成员函数的实例（对象）。

基本作用：

- 它使得成员函数能够访问当前对象的成员变量和其他成员函数。
- 它帮助成员函数区分不同的对象，即使它们具有相同的类类型。

```cpp title="简单this示例"
// x 为类的成员变量
 void setValue(int val) {
    this->x = val;  // 通过 this 指针访问当前对象的成员 x
    // x=val;       // 这样也可以，但是上面写法更容易区分成员变量与其他变量
}
```

`*this`作为重载赋值运算符的返回值，因为它要求返回一个类的引用以支持链式赋值：

```cpp title="*this 返回"
T& operator=(const T& other){
    if(other == *this){return *this}//处理自赋值
    ...
    return *this;
}
T a,b;
...
a = b = T(30);//链式赋值
```

## 常量对象（const object）

- 为了确保 `const` 对象的状态不会被修改，const 对象只能调用类中声明为 const 的成员函数。
- 但是 `mutable` 修饰的成员变量可以在 const 成员函数中被修改：

```cpp
class MyClass {
public:
    void log() const {
        callCount++;  // 合法：mutable 成员变量允许在 const 函数中修改
    }
private:
    mutable int callCount = 0;
};
```

- 同一成员函数可同时有`const`和`非const`版本，编译器会根据调用对象的 const 性自动选择。








# Template（模版）

在 C++ 中，**模板（Template）** 是一种支持**泛型编程**的机制，允许开发者编写与具体类型无关的代码。通过模板，可以定义通用的函数或类，在使用时根据传入的类型或值自动生成对应版本的代码，从而减少重复代码并提高灵活性。




## **模板的类型**
C++ 中主要有两种模板类型：

### 1. **函数模板（Function Template）**

- **定义**：编写一个函数框架，通过**类型参数化**支持多种数据类型。
- **语法**：

     ```cpp
     template <typename T>
     T max(T a, T b) {
         return (a > b) ? a : b;
     }
     ```

- **使用**：

     ```cpp
     int a = 3, b = 5;
     cout << max(a, b);  // 编译器推导 T 为 int
     double x = 2.5, y = 3.7;
     cout << max(x, y);  // T 推导为 double
     ```

### 2. **类模板（Class Template）**

- **定义**：定义一个通用类，成员变量或方法的类型由模板参数决定。
- **语法**：

     ```cpp
     template <typename T>
     class Stack {
     private:
         std::vector<T> elements;
     public:
         void push(T const& elem) {
             elements.push_back(elem);
         }
         T pop() {
             T elem = elements.back();
             elements.pop_back();
             return elem;
         }
     };
     ```

- **使用**：

     ```cpp
     Stack<int> intStack;    // 存储 int 的栈
     Stack<std::string> strStack; // 存储 string 的栈
     ```

---

## **其他模板类型**

1. **可变参数模板（Variadic Template）**  
   支持任意数量和类型的参数，常用于实现递归展开的逻辑（如 `std::make_shared`）：

   ```cpp
   template <typename... Args>
   void print(Args... args) {
       // 使用折叠表达式展开参数包
       (std::cout << ... << args) << "\n";
   }
   ```

2. **非类型模板参数**  
   模板参数可以是具体的值（如整数、指针、枚举），而非类型：

   ```cpp
   template <int N>
   class Array {
       int data[N];  // 固定大小为 N 的数组
   };
   Array<10> arr;    // 生成一个大小为 10 的数组类
   ```

3. **别名模板（Alias Template）**  
   使用 `using` 为模板定义简化别名：

   ```cpp
   template <typename T>
   using Vec = std::vector<T>;  // 别名模板
   Vec<int> v;                  // 等价于 std::vector<int>
   ```

---

## **如何定义模板**

1. **基本语法**  
   - 使用 `template <...>` 声明模板参数列表。
   - 参数可以是类型（`typename T` 或 `class T`）或非类型（如 `int N`）。
   - 示例：

     ```cpp
     template <typename T, int Size>
     class Buffer {
         T data[Size];
         // ...
     };
     ```

2. **显式指定模板参数**  
   如果编译器无法推导类型，需手动指定：

   ```cpp
   template <typename T>
   void logType() {
       std::cout << typeid(T).name() << "\n";
   }
   logType<double>();  // 显式指定 T 为 double
   ```

---

## **何时使用模板？**
模板的典型应用场景包括：

1. **通用容器**  
   如 `std::vector<T>`、`std::map<K, V>`，支持存储任意类型的数据。

2. **通用算法**  
   如 `std::sort`、`std::find`，可处理不同数据类型的集合。

3. **避免代码重复**  
   当多个函数或类逻辑相同，仅类型不同时（例如 `max(int, int)` 和 `max(double, double)`）。

4. **元编程与编译时计算**  
   利用模板在编译期生成代码（如 `std::tuple`、`std::enable_if`）。

---

## **模板的优缺点**

- **优点**：
  - 提高代码复用性，减少冗余。
  - 支持类型安全的泛型操作。
  - 编译时多态，无运行时开销。

- **缺点**：
  - 编译时间可能显著增加。
  - 错误信息晦涩难懂（尤其是模板嵌套时）。
  - 过度使用可能导致代码膨胀（生成过多实例化版本）。

---

## **总结**
模板是 C++ 泛型编程的核心工具，通过将类型参数化，可以实现高度灵活且类型安全的代码。合理使用模板能够大幅提升代码的抽象能力和复用性，但需权衡编译时间和代码复杂度。


注意：

- 模板类的成员函数定义（包括构造函数、析构函数等）必须直接写在头文件中，不能分离到 .cpp 文件。这是因为模板需要编译器在实例化时（如 Vector<int>）能够看到完整的定义。



# 异常处理

C++ 的异常处理机制提供了一种结构化方式来处理运行时错误，允许程序在检测到错误时将控制权转移给专门的错误处理代码。
其核心由三个关键字组成：`try`、`catch` 和 `throw`。

## 1. **基本组件**

- **`throw`**：抛出异常
  当检测到错误时，使用 `throw` 关键字抛出异常对象（可以是任意类型，但推荐使用标准异常类或自定义类）。

  ```cpp
  if (error_occurred) {
      throw std::runtime_error("Error message");
  }
  ```

- **`try`**：监控可能抛出异常的代码块  
  将可能引发异常的代码包裹在 `try` 块中。

  ```cpp
  try {
      // 可能抛出异常的代码
      risky_function();
  }
  ```

- **`catch`**：捕获并处理异常  
  定义处理特定类型异常的代码块，紧跟在 `try` 块后。

  ```cpp
  catch (const std::exception& e) {
      std::cerr << "Exception caught: " << e.what() << std::endl;
  }
  ```

---

## 2. **异常处理流程**

1. 代码在 `try` 块中执行。
2. 若 `try` 块内抛出异常：
   - 立即退出 `try` 块，在调用栈中查找匹配的 `catch` 处理器。
   - 栈展开（Stack Unwinding）：销毁局部对象（调用析构函数）。
3. 按顺序检查 `catch` 块，匹配异常类型（支持继承关系）。
4. 执行匹配的 `catch` 块代码。
5. 若未找到匹配的处理器，调用 `std::terminate()` 终止程序。

---

## 3. **标准异常类**
C++ 标准库在 `<stdexcept>` 中定义了一组异常类（继承自 `std::exception`）：

- **逻辑错误**（通常可预防）：
  - `std::logic_error`、`std::invalid_argument`、`std::out_of_range`
- **运行时错误**（难以预防）：
  - `std::runtime_error`、`std::overflow_error`、`std::underflow_error`
  
**常用方法**：

- `what()`：返回错误描述字符串（需重写）。

  ```cpp
  class MyException : public std::exception {
  public:
      const char* what() const noexcept override {
          return "Custom error message";
      }
  };
  ```

---

## 4. **高级用法**

- **捕获所有异常**：  

  ```cpp
  catch (...) {
      std::cerr << "Unknown exception!" << std::endl;
  }
  ```

- **重新抛出异常**：  
  在 `catch` 块中用 `throw;` 将当前异常传递给上层。
  ```cpp
  catch (const std::exception& e) {
      // 部分处理
      throw; // 重新抛出同一异常
  }
  ```

- **资源管理（RAII）**：  
  利用析构函数自动释放资源（如智能指针、文件句柄），确保异常安全。
  ```cpp
  {
      std::fstream file("data.txt");
      // 若此处抛出异常，file 析构时会自动关闭文件
  }
  ```


## 5. **最佳实践**
1. **避免抛出原始类型**（如 `throw 42;`），使用标准异常或自定义类。
2. **按异常类型从具体到抽象排序** `catch` 块：
   ```cpp
   catch (const MyException& e) { /* 处理具体异常 */ }
   catch (const std::exception& e) { /* 处理通用异常 */ }
   catch (...) { /* 兜底处理 */ }
   ```
3. **确保析构函数不抛出异常**（C++ 中析构函数默认 `noexcept`）。
4. **慎用异常**：高频路径中异常开销较大，建议用于真正异常情况。


## 关键点总结
| 特性          | 说明                                                                 |
|---------------|----------------------------------------------------------------------|
| 栈展开        | 抛出异常时，局部对象自动销毁（析构函数调用）。                       |
| 异常类型匹配  | `catch` 块按声明顺序匹配，支持继承（派生类异常可被基类处理器捕获）。 |
| 异常安全      | 通过 RAII 确保资源泄漏。                                             |
| `noexcept`    | C++11 引入，声明函数不抛出异常（违反时调用 `std::terminate`）。       |

## 示例

### 1. 捕获特定标准异常类型

```cpp
#include <iostream>
#include <stdexcept>
#include <fstream>

int main() {
    try {
        std::ifstream file("nonexistent.txt");
        if (!file) 
            throw std::runtime_error("File open failed");
        
        int value = 120;
        if (value > 100)
            throw std::out_of_range("Value exceeds limit");
    }
    catch (const std::runtime_error& e) {
        std::cerr << "Runtime Error: " << e.what() << std::endl;
    }
    catch (const std::out_of_range& e) {
        std::cerr << "Range Error: " << e.what() << std::endl;
    }
    return 0;
}
```

### 2. 捕获自定义异常类

```cpp
#include <iostream>
#include <string>

// 自定义异常类
class NetworkException : public std::exception {
    std::string msg;
public:
    NetworkException(const std::string& host) 
        : msg("Connection failed to " + host) {}
    
    const char* what() const noexcept override {
        return msg.c_str();
    }
};

void connectToServer(const std::string& host) {
    if (host == "localhost") 
        throw NetworkException(host);
}

int main() {
    try {
        connectToServer("localhost");
    }
    catch (const NetworkException& e) {
        std::cerr << "Network Exception: " << e.what() << std::endl;
    }
    return 0;
}
```

### 3. 捕获基类异常 (多态处理)

```cpp
#include <iostream>
#include <exception>

class BaseException : public std::exception {};
class DerivedException : public BaseException {};

int main() {
    try {
        throw DerivedException(); // 抛出派生类异常
    }
    catch (const BaseException& e) { // 捕获基类引用
        std::cerr << "Caught BaseException (polymorphic handling)\n";
    }
    return 0;
}
```

### 4. 捕获所有异常（通用处理）

```cpp
#include <iostream>
#include <vector>

int main() {
    try {
        std::vector<int> vec;
        vec.at(10) = 5; // 抛出 std::out_of_range
    }
    catch (...) { // 捕获所有异常
        std::cerr << "Unknown exception occurred!" << std::endl;
        throw; // 重新抛出异常
    }
    return 0;
}
```

### 5. 按值捕获 vs 按引用捕获

```cpp
#include <iostream>

int main() {
    try {
        throw std::string("Important error details");
    }
    catch (std::string e) { // 按值捕获（产生拷贝）
        std::cerr << "Caught by value: " << e << std::endl;
    }
    try {
        throw std::string("Important error details");
    }
    catch (const std::string& e) { // 按引用捕获（推荐方式）
        std::cerr << "Caught by reference: " << e << std::endl;
    }
    return 0;
}
```

### 6. 捕获不同数据类型的异常

```cpp
#include <iostream>

void processInput(int code) {
    if (code == 0) throw 404;
    if (code == 1) throw "Invalid parameter";
    if (code == 2) throw 3.14;
}

int main() {
    for (int i = 0; i < 3; ++i) {
        try {
            processInput(i);
        }
        catch (int errCode) {
            std::cerr << "Error code: " << errCode << std::endl;
        }
        catch (const char* msg) {
            std::cerr << "Message: " << msg << std::endl;
        }
        catch (...) {
            std::cerr << "Unexpected error type" << std::endl;
        }
    }
    return 0;
}
```

### 7. 带条件的异常捕获 (C++17)

```cpp
#include <iostream>
#include <system_error>

std::errc checkFile(int status) {
    if (status == 0) return std::errc::no_such_file_or_directory;
    return std::errc::permission_denied;
}

int main() {
    try {
        throw std::make_error_code(checkFile(0));
    }
    catch (const std::error_code& e) 
        if (e == std::errc::no_such_file_or_directory) 
    {
        std::cerr << "File not found!" << std::endl;
    }
    catch (const std::error_code& e) 
        if (e == std::errc::permission_denied) 
    {
        std::cerr << "Access denied!" << std::endl;
    }
    return 0;
}
```

### 总结

1. **精确匹配**：优先使用特定异常类型捕获（如 `std::runtime_error`）
2. **多态处理**：通过基类引用捕获派生类异常（如 `catch (const std::exception&)`）
3. **引用捕获**：总是使用 `const &` 避免不必要的拷贝
4. **异常链**：使用 `throw;` 保留原始异常信息
5. **兜底处理**：`catch (...)` 作为最后的防线
6. **类型安全**：避免捕获基本类型（如 `int`），使用标准/自定义异常类
7. **C++17特性**：带条件的异常捕获（`if` 子句）

> **最佳实践**：异常处理顺序应从具体到抽象。

## 异常规范

# JavaScript介绍



## 变量

`var`由于有“变量提升”等特性不是很好用，建议用`let`关键字声明变量。


## 字符串


### 一、字符串的创建

1. **字面量**：

   ```javascript
   let str1 = '单引号';
   let str2 = "双引号";
   let str3 = `模板字符串`; // ES6
   ```

2. **构造函数**：

   ```javascript
   let str = new String("字符串对象"); // 返回对象类型（非基本字符串）
   ```

3. **字符串的不可变性**：字符串一旦创建，内容不可更改，所有操作返回新字符串。

---

### 二、字符串属性

- **`length`**：返回字符串长度。

  ```javascript
  console.log("hello".length); // 5
  ```

---

### 三、字符串方法

#### 1. 字符访问

- **`charAt(index)`**：返回指定位置的字符。
- **`charCodeAt(index)`**：返回字符的 Unicode 编码。
- **`codePointAt(index)`**：处理 Unicode 大于 0xFFFF 的字符（如表情符号）。
- **`str[index]`**：类似数组索引访问（ES5+）。

#### 2. 字符串连接

- **`concat(str1, str2, ...)`**：拼接字符串（更常用 `+` 或模板字符串）。

  ```javascript
  "Hello".concat(" ", "World"); // "Hello World"
  ```

#### 3. 子字符串查找

- **`indexOf(searchStr[, start])`**：返回首次出现的位置，未找到返回 `-1`。
- **`lastIndexOf(searchStr[, start])`**：从后向前搜索。
- **`includes(searchStr[, start])`**：返回布尔值（ES6）。
- **`startsWith(searchStr[, start])`** / **`endsWith(searchStr[, length])`**：检查开头/结尾（ES6）。
- **`match(regexp)`**：返回正则匹配结果数组。
- **`search(regexp)`**：返回匹配到的位置索引。

#### 4. 截取与分割

- **`slice(start, end)`**：支持负数（从末尾计算）。
- **`substring(start, end)`**：负数视为 `0`，自动交换参数。
- **`substr(start, length)`**：第二个参数为长度（非标准，避免使用）。
- **`split(separator[, limit])`**：按分隔符分割为数组。

  ```javascript
  "a,b,c".split(","); // ["a", "b", "c"]
  ```

#### 5. 替换与大小写转换

- **`replace(searchValue, replaceValue)`**：替换第一个匹配项（支持正则）。
- **`replaceAll(searchValue, replaceValue)`**：替换所有匹配项（ES2021）。
- **`toUpperCase()`** / **`toLowerCase()`**：转换大小写。
- **`toLocaleUpperCase()`** / **`toLocaleLowerCase()`**：地区特定转换。

#### 6. 去除空白

- **`trim()`**：去除两端空白。
- **`trimStart()`** / **`trimEnd()`**：去除开头/结尾空白（ES10）。

#### 7. 其他实用方法

- **`repeat(n)`**：重复字符串 `n` 次（ES6）。

  ```javascript
  "na".repeat(3); // "nanana"

  ```

- **`padStart(length, padStr)`** / **`padEnd(length, padStr)`**：填充字符串到指定长度（ES8）。

  ```javascript
  "5".padStart(3, '0'); // "005"
  ```

- **`localeCompare(targetStr)`**：本地化比较字符串顺序。

---

### 四、模板字符串（ES6+）
1. **多行字符串**：

   ```javascript
   let multiLine = `第一行
   第二行`;
   ```

2. **嵌入表达式**：

   ```javascript
   let name = "Alice";
   console.log(`Hello, ${name}!`); // "Hello, Alice!"
   ```

3. **标签模板**：

   ```javascript
   function tag(strings, ...values) {
     // strings 是静态部分数组，values 是动态表达式结果
     return strings[0] + values[0];
   }
   tag`Hello ${name}!`; // 调用标签函数
   ```

---

### 五、字符串与 Unicode
- **`String.fromCharCode(code1, code2...)`**：将 Unicode 编码转为字符。
- **`String.fromCodePoint(code1, code2...)`**：支持大于 0xFFFF 的码点（ES6）。
- **`normalize(form)`**：标准化 Unicode 字符（如 NFC/NFD 格式）。

---

### 六、类型转换
- **其他类型 → 字符串**：

  ```javascript
  String(123); // "123"
  (123).toString(); // "123"
  `${123}`; // 模板字符串转换
  ```

- **字符串 → 数字**：

  ```javascript
  parseInt("123"); // 123
  parseFloat("3.14"); // 3.14
  Number("42"); // 42
  +"42"; // 42（一元运算符）
  ```

---

### 七、字符串遍历
- **`for...of`** 循环：

  ```javascript
  for (const char of "Hello") { console.log(char); }
  ```

- **转为数组**：

  ```javascript
  [..."Hello"]; // ["H", "e", "l", "l", "o"]
  Array.from("Hello"); 
  "Hello".split("");
  ```

---

### 八、注意事项
- 字符串比较使用 `===`，避免使用 `new String()` 对象（`"a" !== new String("a")`）。
- 优先使用模板字符串代替拼接，提高可读性。
- 涉及正则替换时，可用 `/g` 标志实现全局替换（如 `replace(/a/g, "b")`）。

---

以上内容涵盖了 JavaScript 字符串的核心知识点，适用于日常开发与面试准备。



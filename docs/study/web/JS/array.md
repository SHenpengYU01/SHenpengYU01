# 数组

以下是 JavaScript 中数组（Array）的全面总结，涵盖基础操作、核心方法和高级特性：

---

### **一、数组的创建**
#### 1. 字面量创建
```javascript
const arr1 = [];         // 空数组
const arr2 = [1, 2, 3];  // 含初始值
```

#### 2. 构造函数创建
```javascript
const arr3 = new Array();        // 空数组
const arr4 = new Array(5);       // 长度5的空数组（稀疏数组）
const arr5 = new Array(1, 2, 3); // [1, 2, 3]
```

#### 3. ES6+ 创建方法
```javascript
Array.of(7);       // [7]（解决 new Array(7) 的歧义）
Array.from("abc"); // ['a', 'b', 'c']（类数组转数组）
```

---

### **二、核心操作**
#### 1. 访问元素
```javascript
const arr = [10, 20, 30];
console.log(arr[1]);    // 20
console.log(arr.at(-1)); // 30（ES2022 支持负数索引）
```

#### 2. 修改元素
```javascript
arr[1] = 99; // [10, 99, 30]
```

#### 3. 长度操作
```javascript
arr.length = 2; // 截断数组 → [10, 99]
arr.push(40);   // 末尾添加 → [10, 99, 40]
```

---

### **三、常用方法**
#### 1. 增删元素
| 方法               | 作用                          | 示例                     |
|--------------------|-----------------------------|--------------------------|
| `push(item)`       | 末尾添加元素（返回新长度）          | `arr.push(4)` → 长度+1  |
| `pop()`            | 删除末尾元素（返回被删元素）         | `arr.pop()` → 40        |
| `unshift(item)`    | 开头添加元素（返回新长度）          | `arr.unshift(0)` → 长度+1|
| `shift()`          | 删除开头元素（返回被删元素）         | `arr.shift()` → 0       |
| `splice(start, deleteCount, ...items)` | 增删/替换元素 | `arr.splice(1, 1, 50)` → 替换索引1元素为50 |

#### 2. 遍历方法
| 方法               | 作用                          | 示例                     |
|--------------------|-----------------------------|--------------------------|
| `forEach(callback)` | 遍历元素（无返回值）             | `arr.forEach(v => console.log(v))` |
| `map(callback)`     | 映射新数组                     | `arr.map(v => v * 2)` → 新数组    |
| `filter(callback)`  | 过滤符合条件的元素               | `arr.filter(v => v > 10)` → 新数组|
| `find(callback)`    | 查找第一个符合条件的元素           | `arr.find(v => v > 15)` → 20      |
| `reduce(callback, initialValue)` | 累计计算        | `arr.reduce((sum, v) => sum + v, 0)` → 总和 |

#### 3. 查找与判断
| 方法               | 作用                          | 示例                     |
|--------------------|-----------------------------|--------------------------|
| `includes(value)`  | 是否包含某元素（ES7）           | `arr.includes(20)` → true|
| `indexOf(value)`   | 返回元素首次出现的索引            | `arr.indexOf(20)` → 1    |
| `some(callback)`   | 是否有元素满足条件               | `arr.some(v => v > 30)` → false|
| `every(callback)`  | 是否所有元素都满足条件            | `arr.every(v => v > 5)` → true|

#### 4. 排序与反转
```javascript
const nums = [3, 1, 4];
nums.sort((a, b) => a - b); // [1, 3, 4]
nums.reverse();             // [4, 3, 1]
```

---

### **四、ES6+ 新增方法**
| 方法                | 作用                          | 示例                     |
|---------------------|-----------------------------|--------------------------|
| `flat(depth)`       | 扁平化数组（默认深度1）          | `[1, [2]].flat()` → [1, 2]|
| `flatMap(callback)` | 映射后扁平化                   | `[2, 3].flatMap(x => [x, x*2])` → [2,4,3,6]|
| `findIndex(callback)`| 返回第一个符合条件的元素索引       | `[5, 12].findIndex(v => v > 10)` → 1|
| `fill(value, start, end)` | 填充数组区间          | `new Array(3).fill(0)` → [0,0,0]|
| `Array.isArray(obj)`| 判断是否为数组                 | `Array.isArray([])` → true|

---

### **五、高级特性**
#### 1. 稀疏数组
```javascript
const sparseArr = [1, , 3]; // 中间有空位
console.log(sparseArr.length); // 3
console.log(sparseArr[1]);     // undefined
```

#### 2. 类型化数组（TypedArray）
用于处理二进制数据（如 `Int32Array`, `Uint8Array`）：
```javascript
const buffer = new ArrayBuffer(16);
const int32View = new Int32Array(buffer);
```

#### 3. 迭代器接口
```javascript
for (const item of arr) { /* 遍历元素 */ }
const iterator = arr.values(); // 获取迭代器
```

---

### **六、性能优化**
1. **避免 `delete arr[index]`**  
   会留下空位（变成稀疏数组），建议用 `splice`。
2. **预分配大数组长度**  
   `arr.length = 1000;` 比动态扩容更高效。
3. **批量操作优先用 `slice`/`concat`**  
   替代循环操作。

---

### **七、常见误区**
1. **数组与对象的区别**  
   数组是特殊对象，索引为数字属性，有 `length` 自动更新。
2. **深浅拷贝问题**  
   `slice()`、`concat()` 只能浅拷贝，深拷贝需用 `JSON.parse(JSON.stringify(arr))` 或递归。
3. **判断数组类型**  
   不要用 `typeof`（返回 `"object"`），用 `Array.isArray(arr)`。

---

### **八、总结**
- **核心操作**：增删改查、遍历、排序。
- **ES6+ 方法**：`flat`、`find`、`includes` 等提升开发效率。
- **性能注意**：稀疏数组、预分配长度、批量操作。
- **扩展知识**：类型化数组、迭代器、类数组转换（`Array.from`）。




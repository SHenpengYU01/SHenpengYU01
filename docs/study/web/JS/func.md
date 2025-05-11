# 函数

## 函数参数

参数支持剩余参数，默认参数和解构。

```js
(a, b, ...r) => expression
(a = 400, b = 20, c) => expression
([a, b] = [10, 20]) => expression
({ a, b } = { a: 10, b: 20 }) => expression
```

!!! tip
    JS函数的默认参数可以放在参数列表的任意位置而不仅仅是最后，这与Python和C++不同。


### 剩余参数（rest parameters）

```js
function sum(...theArgs) {
  let total = 0;
  for (const arg of theArgs) {
    total += arg;
  }
  return total;
}
console.log(sum(1, 2, 3));
// Expected output: 6
console.log(sum(1, 2, 3, 4));
// Expected output: 10
```

如果函数的**最后一个**命名参数以...为前缀，则它将成为一个由剩余参数组成的**真数组**，其中从0（包括）到theArgs.length（排除）的元素由传递给函数的实际参数提供。

- 剩余参数不仅可用于函数参数，下面是它在对象解构中的应用：

```js
const config = { theme: "dark", fontSize: 14, debug: true };
const { theme, ...options } = config;
// options = { fontSize: 14, debug: true }
```

!!! info "解构赋值"
    解构赋值指从数组或对象中提取值并赋值给变量：
    ```js
    const [x,y]=[1,2];
    ```


## 匿名函数

形如：

```js
(function (){
    alert("hello");
});
```

当一个函数作为了另一个函数参数时会用到匿名函数。

例：

```js
textBox.addEventListener("keydown", function (event) {
  console.log(`You pressed "${event.key}".`);
});

```

## 箭头函数

### 简介

用箭头函数代替上述例子中function

```js
textBox.addEventListener("keydown", (event)=>{
    console.log(`You pressed "${event.key}".`);
});
```

- 如果函数function**只接受一个参数**，可以省略参数周围括号，直接写为`event=>`
- 如果整个函数**只包含一行**return语句，可以省略大括号和`return`关键字，隐式地返回表达式。

```js
const orig = [1,2,3];
const doubled = orig.map(item=>item*2);
```

这就等价于下面两种形式

```js
orig.map(function (item){
    return item*2;
});
orig.map((item)=>{
    return item*2;
});
```

### 形式

```js
() => expression

param => expression

(param) => expression

(param1, paramN) => expression

() => {
  statements
}

param => {
  statements
}

(param1, paramN) => {
  statements
}
```

### 注意

1. 参数和箭头之间不能换行
2. 箭头函数不能用作方法

```js
students.forEach(student=>{回调函数的实现})
```

使用forEach并定义箭头函数单独处理数组中的每个元素。



// // Обычная функция, принимающая один параметр «number». Если функция изменит значение 
// // переменной, переданной как аргумент, то это изменение никак не отразится глобально  
// let number = 10;

// function square(number) { 
//     return number * number;
// }

// console.log(number);
// console.log(square(number));
// console.log(number);

// // Функция, принимающая объект. Она изменяет свойство объекта: это изменение будет 
// // видно глобально

// let car = {
//     make: "Honda",
//     model: "Accord",
//     year: 1998
// };

// function func(objectOfCar) {
//     objectOfCar.make = "Toyota";
// }

// console.log(car.make);
// func(car);
// console.log(car.make);


// // Ананонимная функция (не имеет имени), которая присвоена переменной
// const value = function(number) {
//     return number ** 2;
// }

// console.log(value(4));

// // Функция, которая присвоеной, может иметь имя, чтобы вызвать саму себя внетри себя (рекурсия)

// const factorial = function func(number) {
//     return number < 2 ? 1 : number * func(number - 1); 
// };

// console.log(factorial(5))

// // Второй пример рекурсии
// function map(func, array) {
//     let resultArray = [], i;

//     for (i = 0; i < array.length; i ++) resultArray[i] = func(array[i]);

//     return resultArray;
// }

// const func = function (number) {
//     return number ** 3;
// }

// let array = [0, 1, 3, 4, 5];

// const cube = map(func, array);
// console.log(cube);

// // Вложенная функция. Она имеет доступ ко всем глобальным переменным и переменым ее 
// // родителя, но родитель не имеет доступа к переменным дочерней функции - замыкание
// let num1 = 20, num2, num3;


// function getScore() {
//     num2 = 2;
   
//     function add() {
//         num3 = 23;
//         console.log(num1, num2, num3);
//     }

//     add();

//     console.log(num1, num2, num3);
// }

// getScore();

// // При вызове внешней функции можно указать аргументы как для внешней, так и для 
// // внутренней функции.
// function outside(x) {
//     function inside(y) {
//         return x + y;
//     }

//     return inside;
// }

// fn_inside = outside(3);
// result = fn_inside(5);
// result1 = outside(3)(5);
// result2 = outside(3).

// console.log(result, result1);

// // Переменные и функции продолжают существовать после выполнения внешней функции, 
// // потому что внутренняя функции имеет доступ к scope внешней
// let pet = function(name) {
//     let getName = function() {
//         return name
//     }

//     return getName;
// }

// let myPet = pet("Vivie");
// console.log(myPet());

// // Более сложный пример
// let createPet = function(name) {
//     let sex;

//     return {
//         setName: function(newName) {
//             name = newName;
//         },
        
//         getName: function() {
//             return name;
//         },

//         setSex: function(newSex) {
//             if (
//                 typeof newSex === "string" && 
//                 (newSex.toLowerCase() === "male" || newSex.toLowerCase() === "female")
//             ) {
//                 sex = newSex;
//             }
//         },

//         getSex: function() {
//             return sex;
//         }
//     }
// }

// let pet = createPet("Vivie");
// console.log(pet.getName());

// pet.setName("Pliver");
// pet.setSex("male");
// console.log(pet.getName());
// console.log(pet.getSex());

// // arguments - псевдо-класс для получения доступа к параметрам функции 
// function myConcat(separator) {
//     let result = "";

//     for (let i = 1; i < arguments.length; i++) {
//         result += arguments[i] + separator;
//     }

//     return result;
// }

// console.log(myConcat(", ", "red", "orange", "blue"));


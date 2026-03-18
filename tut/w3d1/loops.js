const arr = ["A", "B", "C"];
const obj = { x: 1, y: 2 };

for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

let count = 0;
while (count < 2) {
  count++;
}

let j = 5;
do {
  j++;
} while (j < 5);

for (const item of arr) {
  console.log(item); 
}

for (const key in obj) {
  console.log(`${key}: ${obj[key]}`); 
}

outerLoop: for (let a = 0; a < 3; a++) {
  for (let b = 0; b < 3; b++) {
    if (a === 1 && b === 1) break outerLoop; 
  }
}

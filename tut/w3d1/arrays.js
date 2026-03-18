let nums = [1, 2, 3, 4, 5];

console.log(nums.length); 

nums.push(6);          // Adds to end
nums.pop();            // Removes from end
nums.unshift(0);       // Adds to start
nums.shift();          // Removes from start
nums.splice(2, 1, 99); // Removes 1 item at index 2, inserts 99
nums.reverse();        // Reverses array in place
nums.sort();           // Sorts in place (lexicographically by default)

const sliced = nums.slice(1, 3);      // Extracts a section
const joined = nums.join("-");        // Converts to string: "1-2-3"
const hasThree = nums.includes(3);    // Boolean check
const index = nums.indexOf(99);       // Returns index or -1

// map: Creates new array by transforming each element
const doubled = nums.map(n => n * 2);

// filter: Creates new array with elements that pass a condition
const evens = nums.filter(n => n % 2 === 0);

// reduce: Accumulates array down to a single value
const sum = nums.reduce((total, n) => total + n, 0);

// find: Returns the FIRST element matching a condition
const firstLarge = nums.find(n => n > 3);

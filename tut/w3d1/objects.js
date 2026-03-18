const user = {
    name: "Dave",
    role: "Admin",
    greet() {
        return `Hi, I'm ${this.name}`;
    }
};

console.log(user.name);    // Dot notation
console.log(user["role"]); // Bracket notation (useful for dynamic keys)

// Object.keys: Array of keys -> ["name", "role", "greet"]
const keys = Object.keys(user);

// Object.values: Array of values -> ["Dave", "Admin", [Function: greet]]
const values = Object.values(user);

// Object.entries: Array of key-value pairs -> [["name", "Dave"], ...]
const entries = Object.entries(user);

// Object.assign: Merges objects
const permissions = { canEdit: true };
const mergedUser = Object.assign({}, user, permissions);

// Object.freeze: Prevents adding, removing, or changing properties
Object.freeze(user);
user.name = "Bob"; 

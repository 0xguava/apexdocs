async function demo(){
  try {
    const res = await fetch("https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json");
    console.log(`${res.url} : ${res.status}`);
  } catch(error) {
    console.log(error)
  }
  console.log("completed")
}

demo();
console.log("started")


const fetch_promise = fetch("https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json");

console.log(fetch_promise);

fetch_promise
  .then((response) => {
    console.log(`${response.url} : ${response.status}`);
  })
  .catch((error) => {
    console.log(error);
  })
  .finally(() => {
    console.log("completed")
  });

console.log("started");

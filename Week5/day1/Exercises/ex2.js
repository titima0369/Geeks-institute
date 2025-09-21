const delayedSuccess = new Promise((resolve) => {
  setTimeout(() => {
    resolve("success");
  }, 4000);
});

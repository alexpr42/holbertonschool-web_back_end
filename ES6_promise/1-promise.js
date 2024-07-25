function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    // Simulate an asynchronous operation
    setTimeout(() => {
      const success = true; // Simulate a successful response

      if (success) {
        resolve('Success!');
      } else {
        reject(new Error('Failed!'));
      }
    }, 1000);
  });
}

export default getResponseFromAPI;

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question(`Enter a number:`, (user_hand) => {
  if (Number(user_hand) < 10) {
    conosle.log("Eh...");
  } else {
    console.log("Win somhow!");
  }
  readline.close(); // must end i/o blocking
});

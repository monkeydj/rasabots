#!/usr/bin/env node

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("Enter a number: ", (userInputs) => {
  console.log(checkHands(userInputs));
  readline.close(); // must end i/o blocking
});

function checkHands(userHand, botHand = Math.random()) {
  return Number(userHand) < botHand ? "Eh..." : "Win somhow!";
}

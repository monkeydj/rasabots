#!/usr/bin/env node

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("Enter a number: ", (userInputs) => {
  console.log(checkHands(userInputs));
  readline.close(); // must end i/o blocking
});

function generateBotHand(min = 0, max = 10) {
  return Math.random() * (max - min) + min;
  // I have ridiculously implemented such code countless times...
}

function checkHands(userHand, botHand = generateBotHand()) {
  return userHand < botHand ? "Eh..." : "[!!] Winner [!!]";
}

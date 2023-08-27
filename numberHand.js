#!/usr/bin/env node

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// I have ridiculously implemented such code countless times...
const randRange = (min = 0, max = 10) => Math.random() * (max - min) + min;

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
const waitRandomly = (secs) => delay(randRange(secs * 1e3));

const generateBotHand = (centerPoint = 10) => randRange(0, centerPoint);

readline.question("Enter a number: ", (userInputs) => {
  const userHand = Number(userInputs);
  const botHand = generateBotHand(userHand * 2);

  process.stdout.write("and Bot hand is... ");
  waitRandomly(3).then(() => console.log(`**${botHand}**`));

  console.log(checkHands(userHand, botHand));

  readline.close(); // must end i/o blocking
});

function checkHands(userHand, botHand = generateBotHand()) {
  return userHand < botHand ? "Eh..." : "[!!] Winner [!!]";
}

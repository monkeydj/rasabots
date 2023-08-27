#!/usr/bin/env node

const { execSync } = require("child_process");

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// I have ridiculously implemented such code countless times...
const randRange = (min = 0, max = 10) => Math.random() * (max - min) + min;
// const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
// const waitRandomly = (secs) => delay(randRange(secs * 1e3));
const waitRandomlySync = (secs) => execSync(`sleep ${randRange(secs)}`);

const generateBotHandByCentre = (aNumber = 10) => randRange(0, aNumber * 2);

readline.question("Enter a number: ", (userInputs) => {
  const userHand = Number(userInputs);
  const botHand = generateBotHandByCentre(userHand);

  process.stdout.write("and Bot hand is... ");
  waitRandomlySync(3);

  console.log(`**${botHand}**`);
  console.log(checkHands(userHand, botHand));

  readline.close(); // must end i/o blocking
});

function checkHands(userHand, botHand = generateBotHand()) {
  return userHand < botHand ? "Eh..." : "[!!] Winner [!!]";
}

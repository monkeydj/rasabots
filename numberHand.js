#!/usr/bin/env node

// --- required modules ---

const { execSync } = require("child_process");

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// --- main application starts ---

const randRange = (min = 0, max = 10) => Math.random() * (max - min) + min;
// * keep following 2 lines for references
// const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
// const waitRandomly = (secs) => delay(randRange(secs * 1e3));
// * following will block the whole running process
const waitRandomlySync = (secs) => execSync(`sleep ${randRange(secs)}`);
// ref: https://masteringjs.io/tutorials/node/sleep

readline.question("Enter a number: ", (userInputs) => {
  const userHand = Number(userInputs);
  const botHand = generateBotHandByCentre(userHand);

  console.log(checkHands(userHand, botHand)); // ? main game

  readline.close(); // must end i/o blocking
});

function generateBotHandByCentre(aNumber = 10) {
  const botHand = randRange(0, aNumber * 2);

  process.stdout.write("and Bot hand is... ");
  waitRandomlySync(3);
  // ! look good but truly violate pure function
  console.log(`**${botHand}**`);

  return botHand;
}

function checkHands(userHand, botHand = generateBotHand()) {
  return userHand < botHand ? "Eh..." : "[!!] Winner [!!]";
}

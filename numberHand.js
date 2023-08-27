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

  showHand(botHand, "and Bot hand is...");

  console.log(checkHands(userHand, botHand)); // ? main game

  readline.close(); // must end i/o blocking
});

function template(strings, ...keys) {
  // * have funs with template literals
  // ref: [Tag functions don't even need to return a string!]
  // ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
  return (...values) => {
    const dict = values[values.length - 1] || {};
    const result = [strings[0]];
    keys.forEach((key, i) => {
      const value = Number.isInteger(key) ? values[key] : dict[key];
      result.push(value, strings[i + 1]);
    });
    return result.join("");
  };
}

function showHand(aHand, introduce = 'once upon a time... there is a hand [${"aHand"}]') {
  const introduction = template`${introduce}`(aHand);
  console.log(introduction);
  waitRandomlySync(3);
  // ! look good but truly violate pure function
  console.log(`[${aHand}]`);
}

function generateBotHandByCentre(aNumber = 10) {
  return randRange(0, aNumber * 2);
}

function checkHands(userHand, botHand = generateBotHand()) {
  return userHand < botHand ? "Eh..." : "[!!] Winner [!!]";
}

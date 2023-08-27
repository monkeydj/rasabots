#!/usr/bin/env node

// --- required modules ---

const { execSync } = require("child_process");

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

// --- main application starts ---

const generateBotHandByCentre = (aNumber = 10) => randRange(0, aNumber * 2);
const checkHands = (userHand, botHand = generateBotHand()) => {
  const result = userHand < botHand ? "Eh..." : "[!!] Winner [!!]";
  console.log(result);
};

const showHand = (aHand, introduce = template`got a hand [${"aHand"}]`) =>
  typeof introduce === "function"
    ? console.log(introduce({ aHand }))
    : process.stdout.write(introduce) && waitRandomlySync(3) && console.log(`[${aHand}]`);

readline.question("Enter a number: ", (userInputs) => {
  const userHand = Number(userInputs);
  const botHand = generateBotHandByCentre(userHand);

  showHand(botHand, "and Bot hand is...");
  checkHands(userHand, botHand);

  readline.close(); // must end i/o blocking
});

// --- partition for utility functions ---

function randRange(min = 0, max = 10) {
  return Math.random() * (max - min) + min;
}

// * keep following lines for references
// function delay (ms) { return new Promise((resolve) => setTimeout(resolve, ms));}
// function waitRandomly (secs) { return delay(randRange(secs * 1e3));}

// * following will block the whole running process
// ref: https://masteringjs.io/tutorials/node/sleep
function waitRandomlySync(secs) {
  return execSync(`sleep ${randRange(secs)}`);
}

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

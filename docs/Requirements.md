# Requirements

## MVP

- create Python scraper that navigates to [MDN HTML Element reference page](https://developer.mozilla.org/en-US/docs/Web/HTML/Element), grabs all the elements from the _HTML elements_ list & populates the `htmlElementReference.json` file,
- when the user starts the game, a timer is set in action
- the game consists of submitting **HTML** element names using the keyboard
- the game tracks the progress of the current session in the form of a percentage (no. of correct submissions / total no. of HTML elements)
- the game stops if
  - the user chooses to forfeit the current session
  - the time runs out
  - or all the **HTML** elements have been submitted
- resubmitting an element that was already submitted brings no penalty

## Nice to have

- the user should be able to select between 3 levels of difficulty that differ between them by the amount of time available
  - novice
  - intermediate
  - grandmaster
- ❓ the current session progress percentage is broken down into four categories:
  - **experimental**
  - **deprecated**
  - **non-standard**
  - **standard**
- ❓ the correct submissions should be tracked into four categories
  - **experimental**
  - **deprecated**
  - **non-standard**
  - **standard**
- the game should signal to the user how much time is left through a background color
  - 100% - 50% green
  - 50% - 25% orange
  - 25% - 0% red

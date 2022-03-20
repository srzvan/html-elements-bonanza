var state = [...htmlElements];

const startTimerBtn = document.querySelector(".start-timer");
startTimerBtn.addEventListener("click", () => timer());

const input = document.querySelector("#html-element");
input.addEventListener("keydown", event => {
  const { target, key } = event;
  const container = document.querySelector(".named-elements");

  if (key === "Enter") {
    inputHandler(container, target.value);
    target.value = "";
  }
});

function timer(seconds = 300) {
  let s = seconds;

  renderTime(s);
  s -= 1;

  const interval = setInterval(() => {
    if (s == 0) {
      clearInterval(interval);
    }

    renderTime(s);

    s -= 1;
  }, 1000);

  function renderTime(seconds) {
    const TEXT_COLORS = {
      orange: "orange",
      red: "red",
    };
    const elem = document.querySelector(".timer > span");

    if (s <= 45 && s > 15) {
      elem.style.color = TEXT_COLORS.orange;
    } else if (s <= 15) {
      elem.style.color = TEXT_COLORS.red;
    }

    elem.textContent = seconds;
  }
}

function inputHandler(container, value) {
  const index = state.findIndex(element => element.name === value);

  if (index !== -1) {
    removeNamedHtmlElement(index);
    renderNamedElement(container, value);
  }

  function renderNamedElement(container, elName) {
    const span = document.createElement("span");
    span.innerText = elName;

    container.appendChild(span);
  }

  function removeNamedHtmlElement(index) {
    state.splice(index, 1);
  }
}

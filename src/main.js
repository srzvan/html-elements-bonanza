let intervalId = null;
const startButton = document.getElementsByName('start-button')[0];
startButton.addEventListener('click', timer);

function timer() {
  if (intervalId !== null) {
    return;
  }

  startButton.classList.add('hidden');
  const timeInSeconds = 10;

  const timerElement = document.getElementsByClassName('timer')[0];
  const gameElement = document.getElementsByClassName('game')[0];
  gameElement.classList.remove('hidden');

  intervalId = setInterval(() => {
    --timeInSeconds;
    updateTimerElement(timeInSeconds);

    if (timeInSeconds === 0) {
      clearInterval(intervalId);
    }
  }, 1000);

  function updateTimerElement(time) {
    const minutes = Math.floor(time / 60);
    const seconds = time % 60;

    timerElement.innerText = `${minutes}:${formatSeconds(seconds)}`;

    function formatSeconds(seconds) {
      return seconds < 10 ? `0${seconds}` : seconds;
    }
  }
}

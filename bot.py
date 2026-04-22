<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dog Clicker Pro</title>

<style>
body {
  margin: 0;
  font-family: Arial;
  text-align: center;
  background: #0f0f0f;
  color: white;
}

h1 {
  margin-top: 15px;
}

#score {
  font-size: 32px;
  margin: 10px;
}

#persec {
  color: #aaa;
  margin-bottom: 10px;
}

img {
  width: 220px;
  border-radius: 20px;
  cursor: pointer;
  transition: 0.1s;
  margin-top: 20px;
}

img:active {
  transform: scale(0.95);
}

/* SHOP */
.shop {
  margin-top: 30px;
  background: #1c1c1c;
  padding: 15px;
  border-radius: 15px;
  width: 90%;
  max-width: 400px;
  margin-left: auto;
  margin-right: auto;
}

button {
  width: 100%;
  padding: 10px;
  margin-top: 10px;
  border: none;
  border-radius: 10px;
  background: #4caf50;
  color: white;
  font-size: 16px;
}
button:active {
  transform: scale(0.98);
}
</style>
</head>

<body>

<h1>🐶 Dog Clicker Pro</h1>

<div id="score">0 🦴</div>
<div id="persec">0 / sec</div>

<img id="dog" src="https://i.imgur.com/4AiXzf8.jpeg">

<div class="shop">
  <h3>🛒 Магазин</h3>

  <button onclick="buyClick()">
    +1 к клик (Цена: <span id="clickCost">10</span>)
  </button>

  <button onclick="buyAuto()">
    Авто доход +1/сек (Цена: <span id="autoCost">25</span>)
  </button>
</div>

<script>
let score = 0;
let clickPower = 1;
let autoPower = 0;

let clickCost = 10;
let autoCost = 25;

// загрузка
if (localStorage.getItem("game")) {
  const data = JSON.parse(localStorage.getItem("game"));
  score = data.score;
  clickPower = data.clickPower;
  autoPower = data.autoPower;
  clickCost = data.clickCost;
  autoCost = data.autoCost;
}

const dog = document.getElementById("dog");
const scoreText = document.getElementById("score");
const persecText = document.getElementById("persec");

const clickCostText = document.getElementById("clickCost");
const autoCostText = document.getElementById("autoCost");

// клик
dog.onclick = () => {
  score += clickPower;
  update();
};

// магазин
function buyClick() {
  if (score >= clickCost) {
    score -= clickCost;
    clickPower += 1;
    clickCost = Math.floor(clickCost * 1.5);
    update();
  }
}

function buyAuto() {
  if (score >= autoCost) {
    score -= autoCost;
    autoPower += 1;
    autoCost = Math.floor(autoCost * 1.6);
    update();
  }
}

// авто доход
setInterval(() => {
  score += autoPower;
  update();
}, 1000);

// обновление
function update() {
  scoreText.innerText = score + " 🦴";
  persecText.innerText = autoPower + " / sec";

  clickCostText.innerText = clickCost;
  autoCostText.innerText = autoCost;

  localStorage.setItem("game", JSON.stringify({
    score,
    clickPower,
    autoPower,
    clickCost,
    autoCost
  }));
}

update();
</script>

</body>
</html>

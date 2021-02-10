var canvas = document.querySelector('canvas');
var context = canvas.getContext('2d');

var width = canvas.width = window.innerWidth;
var height = canvas.height = window.innerHeight;

var waves = [];
// Change these for more waves or bigger waves
const count = 3;
const waveHeight = 70;
var colors = ['#F2B134', '#068587', '#ED553B'];

window.addEventListener('resize', resizeCanvas, false);

init();


function init() {
  for (let i = 0; i < count; i++) {
    createWave(colors[i], 5);
  }
  setInterval(update, 10);
}


function rnd(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}

function update() {
  context.fillStyle = '#112F41';
  context.globalCompositeOperation = 'source-over';
  context.fillRect(0, 0, width, height);

  context.globalCompositeOperation = 'screen';
  // Draw waves
  for (let i = 0; i < waves.length; i++) {
    for (let j = 0; j < waves[i].nodes.length; j++) {
      bounce(waves[i].nodes[j]);
    }
    drawWave(waves[i]);
  }
}
function createWave(color, nodes) {
  var nodeArray = [];
  for (let i = 0; i <= nodes + 2; i++) {
    // Each node is a set of four points
    var node = [((i - 1) * width) / nodes, 0, Math.random() * 200, 0.3];
    nodeArray.push(node);
  }
  waves.push({
    color: color,
    nodes: nodeArray,
  });
}

function bounce(node) {
  // We change the value of the quadratic pull for each point to move the line
  node[1] = (waveHeight / 2) * Math.sin(node[2] / 20) + height / 2;
  node[2] = node[2] + node[3];
}

function drawWave(wave) {
  var diff = function(a, b) {
    return (b - a) / 2 + a;
  };
  context.fillStyle = wave.color;
  context.beginPath();
  context.moveTo(0, height);
  context.lineTo(wave.nodes[0][0], wave.nodes[0][1]);
  for (let i = 0; i < wave.nodes.length; i++) {
    if (wave.nodes[i + 1]) {
      context.quadraticCurveTo(
        wave.nodes[i][0],
        wave.nodes[i][1],
        diff(wave.nodes[i][0], wave.nodes[i + 1][0]),
        diff(wave.nodes[i][1], wave.nodes[i + 1][1]),
      );
    } else {
      context.lineTo(wave.nodes[i][0], wave.nodes[i][1]);
      context.lineTo(width, height);
    }
  }

  context.closePath();
  context.fill();
}

function resizeCanvas() {
  width = canvas.width = window.innerWidth;
  height = canvas.height = window.innerHeight;
  
  update();
}
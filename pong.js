//Variáveis da bola
let xBola = 300;
let yBola = 200;
let diametroBola = 20;
let raioBola = diametroBola / 2;
let velocidadeX = 10;
let velocidadeY = 4;

//Variáveis das raquetes
let xRaquete1 = 0;
let yRaquete1 = 155;
let xRaquete2 = 592;
let yRaquete2 = 155;
let larguraRaquete = 12;
let alturaRaquete = 90;

let pontos1 = 0;
let pontos2 = 0;

let margemErro = -45;

function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(0);
  rect(296, 0, 8, 400);
  bola();
  raquete1();
  raquete2();
  placar();
}

//Define a bola
function bola(){
  circle(xBola,yBola,diametroBola);
  xBola += velocidadeX;
  yBola += velocidadeY;
  //Faz a bola ricochetear nas bordas
  if(yBola + raioBola >= height || yBola - raioBola <= 0){
    velocidadeY *= -1;
  }
  //Faz a bola ricochetear nas raquetes e os pontos
  if(xBola - raioBola <= xRaquete1 + larguraRaquete){
    xBola = 23;
    velocidadeX *= -1;
    if(yBola + raioBola < yRaquete1 || yBola - raioBola > yRaquete1 + alturaRaquete){
      pontos2++;
    }
  }
  if(xBola + raioBola >= xRaquete2){
    xBola = 577;
    velocidadeX *= -1;
    margemErro = random(-110, 20);
    if(yBola + raioBola < yRaquete2 || yBola - raioBola > yRaquete2 + alturaRaquete){
      pontos1++;
    }
  }
}

//Define a raquete do computador
function raquete1(){
  rect(xRaquete1, yRaquete1, larguraRaquete, alturaRaquete);
  yRaquete1 = yBola + margemErro;
}

//Define a raquete do jogador
function raquete2(){
  rect(xRaquete2, yRaquete2, larguraRaquete, alturaRaquete)
  if(keyIsDown(UP_ARROW)){
    yRaquete2 -= 10;
  }
  if(keyIsDown(DOWN_ARROW)){
    yRaquete2 += 10;
  }
}

//Define o placar
function placar(){
  fill(255);
  textSize(25);
  text(pontos1, 250, 30);
  text(pontos2, 330, 30);
}


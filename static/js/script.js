let bubbles = document.querySelector('.bubbles')


for (let i = 0; i < 8; i++) {
    let bubble = document.createElement('div')
    let posX = Math.random() * 95
    let daley = Math.random() * -50
    let duration = (Math.random() * 25) + 3

    bubble.className = 'bubble'
    bubble.style.left = posX + '%'
    bubble.style.animationDelay = daley + 's'
    bubble.style.animationDuration = duration + 's'


    bubbles.appendChild(bubble)
}







function PolyCalc(f /*a function(t)  from [0, infinity) => [0, 1]*/, 
                  s, /*a slice function(y, i) from y [0,1] => [0, 1], with slice index, i, in [0, n]*/
									w /*window size in seconds*/,
                  n /*sample size*/,
                  o /*orientation => left/right/top/bottom - the 'flat edge' of the polygon*/ 
                  ) 
{
	this.polyStart = "polygon(";
  this.polyLeft = this.polyStart + "0% 0%, "; //starts in the top left corner
  this.polyRight = this.polyStart + "100% 0%, "; //starts in the top right corner
  this.polyTop = this.polyStart + "0% 0%, "; // starts in the top left corner
  this.polyBottom = this.polyStart + "0% 100%, ";//starts in the bottom left corner
  
  var self = this;
  self.mapFunc = s;
  this.func = f;
  this.window = w;
  this.count = n;
  var dt = w/n;  

  switch(o) {
    case "top":
      this.poly = this.polyTop; break;
    case "bottom":
      this.poly = this.polyBottom; break;
  	case "right":
    	this.poly = this.polyRight; break;
  	case "left":
  	default:
  		this.poly = this.polyLeft; break;
    }
    
  this.CalcPolygon = function(t) {
  	var p = this.poly;
    for (i = 0; i < this.count; i++) {
      x = 100 * i/(this.count-1.0);
      y = this.func(t + i*dt);
      if (typeof self.mapFunc !== 'undefined')
      	y=self.mapFunc(y, i);
      y*=100;
      switch(o) {
        case "top": 
          p += x + "% " + y + "%, "; break;
        case "bottom":
          p += x + "% " + (100-y) + "%, "; break;
      	case "right":
        	p += (100-y) + "% " + x + "%, "; break;
      	case "left":
        default:
        	p += y + "% " + x + "%, "; break;          
      }
    }
    
    switch(o) { 
      case "top":
        p += "100% 0%)"; break;
      case "bottom":
        p += "100% 100%)";
        break;
    	case "right":
      	p += "100% 100%)"; break;
    	case "left":
      default:
      	p += "0% 100%)"; break;
    }
    
    return p;
  }
};

var text = document.querySelector("#text");
var divs = document.querySelectorAll(".wave");
var freq=2*Math.PI; //angular frequency in radians/sec
var windowWidth = 1; //the time domain window which determines the range from [t, t+windowWidth] that will be evaluated to create the polygon
var sampleSize = 60;
divs.forEach(function(wave) {
  var loc = wave.classList[1];

  var polyCalc = new PolyCalc(
	  function(t) { //The time domain wave function
  	  return (Math.sin(freq * t) + 1)/2; //sine is [-1, -1], so we remap to [0,1]
    },
    function(y, i) { //slice function, takes the time domain result and the slice index and returns a new value in [0, 1]  
      return MapRange(y, 0.0, 1.0, 0.65, 1.0);  //Here we adjust the range of the wave to 'flatten' it out a bit.  We don't use the index in this case, since it is irrelevant
    },
    windowWidth, //1 second, which with an angular frequency of 2pi rads/sec will produce one full period.
    sampleSize, //the number of samples to make, the larger the number, the smoother the curve, but the more pionts in the final polygon
    loc //the location
  );
  
    var polyText = polyCalc.CalcPolygon(0);
    wave.style.clipPath = polyText;
    wave.style.shapeOutside = polyText;
    wave.addEventListener("click",function(e) {document.querySelector("#polygon").innerText = polyText;});
  });

function MapRange(value, min, max, newMin, newMax) {
  return value * (newMax - newMin)/(max-min) + newMin;
}

//Animation - animate the wave by uncommenting this section
//Also demonstrates a slice function which uses the index of the slice to alter the output for a dampening effect.

var t = 0;
var speed = 1/180;

var polyTop = document.querySelector(".top");

var polyTopCalc = new PolyCalc(
	  function(t) {
  	  return (Math.sin(freq * t) + 1)/2;
    },
    function(y, i) {       
      return MapRange(y, 0.0, 1.0, (sampleSize-i)/sampleSize, 1.0);
    },
    windowWidth, sampleSize, "top"
  );

function animate() {
		var polyT = polyTopCalc.CalcPolygon(t);    
    t+= speed;
    polyTop.style.clipPath = polyT;    
    requestAnimationFrame(animate);
}

requestAnimationFrame(animate)




const links = document.querySelector('.links');
const menu = document.querySelector('.fa-bars');

menu.onclick = () =>{
  links.classList.toggle('active');
  menu.classList.toggle('fa-times');
}



$(document).ready(function () {
  $('.slider').slick({
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 3,
      autoplay: true,
      autoplaySpeed: 2000,
      arrows: false,
      dots: false,
      responsive: [
          {
            breakpoint: 900,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
  });
});

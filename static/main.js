/* Toggle Footer */
//document.getElementById("footer").style.display = "block";

/* 
  fetch('http://192.168.0.130:5000/health').then(response => response.json()) .then(data => console.log(data));
*/

const api_url = 'http://192.168.1.132:5000/data'

async function page_change() {
  const response = await fetch(api_url);
  const data = await response.json();
  console.log(data)
  

  const { num_can, num_plas, status, loader } = data;

  if (status == 'idle') {
    document.getElementById("idle").style.display = "block";
    document.getElementById("home").style.display = "none";
    document.getElementById("count").style.display="none";
    document.getElementById("reward").style.display="none";
  }

  if (status == 'home') {
    document.getElementById("home").style.display = "block";
    document.getElementById("idle").style.display = "none";
    document.getElementById("count").style.display="none";
    document.getElementById("reward").style.display="none";
  }

  if (status == 'count') {
    document.getElementById("home").style.display = "none";
    document.getElementById("idle").style.display = "none";
    document.getElementById("count").style.display="block";
    document.getElementById("reward").style.display="none";
    
    document.getElementById("Plastic").textContent = num_plas;
    document.getElementById("Can").textContent = num_can;

    if (loader == 1) {
      document.getElementById("loader").style.display = "block";
    }
    else {
      document.getElementById("loader").style.display = "none";
    }
  }

  if (status == 'reward') {
    document.getElementById("home").style.display = "none";
    document.getElementById("idle").style.display = "none";
    document.getElementById("count").style.display="none";
    document.getElementById("reward").style.display="block";
  }
}

page_change();
setInterval(page_change, 1000)

function clicked() {
  fetch('http://192.168.1.132:5000/stop').then(response => response.json())
}
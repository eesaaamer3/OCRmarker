// imports nodeJS modules
var { PythonShell } = require("python-shell");
const fs  = require('fs')

// Uses python shell to create a function that runs the python script "argument.py"
function triggerPythonCode(){
  PythonShell.run('argument.py', null, function (err) {
    if (err) throw err;
    console.log('finished');
  });
}


// Submits all document values at once from the JavaScript form in "index.html"
function submitAll(){
  let q1 = document.getElementById("hello1").value
  let q2 = document.getElementById("hello2").value
  let q3 = document.getElementById("hello3").value

}

// Holds the main answer key
let Answers = []

// Writes answers to a seperate text file "textfile.txt"
function writePython() {
    fs.appendFileSync("textfile.txt", document.getElementById("name-of-student").value);
    fs.appendFileSync("textfile.txt", "\n");

    fs.appendFileSync("textfile.txt", document.getElementById("assessment-id").value);
    fs.appendFileSync("textfile.txt", "\n");

    for (i = 0; i < Answers.length; i++){
        fs.appendFileSync("textfile.txt", Answers[i], "utf-8");
        fs.appendFileSync("textfile.txt", "\n");
    }
  
    // executes the python code
  triggerPythonCode();
}


function getData1() {
    i = 0
    var x = document.getElementsByClassName("first-input");
    Array.prototype.forEach.call(x, function(el) {
            Answers.push(x[i].value)
            i++
    });
    console.log(Answers)
}

function getData2() {
    i = 0
    var x = document.getElementsByClassName("second-input");
    Array.prototype.forEach.call(x, function(el) {
            Answers.push(x[i].value)
            i++
    });
    console.log(Answers)
}



function getData3() {
    i = 0
    var x = document.getElementsByClassName("third-input");
    Array.prototype.forEach.call(x, function(el) {
            Answers.push(x[i].value)
            i++
    });
    console.log(Answers);
    writePython()
}



function num_questions1() {
    let style = "margin-top: 5px; margin-bottom: 10px"
    var q = 1
    let num = document.getElementById("hello1").value;
    let j = document.createElement("button");
    j.innerHTML = "Submit";
    j.setAttribute("onclick", "getData1();");

    for (let i = 0; i< num; i++){ 
        let dad = document.getElementById("questions1");
            
        let i = document.createElement("input");
        
                
        let apple = document.createTextNode("Question #" + q + " Answer Here: ");
        let k = document.createElement("br");
            
        i.innerHTML = "ko";
        
        i.setAttribute("class", "first-input")
                
        i.style = style
        dad.appendChild(k);
        dad.appendChild(apple);
        dad.appendChild(i);
        dad.appendChild(j);
        dad.appendChild(k);
        dad.appendChild(k);
        dad.appendChild(k);
        
        q++

    }

    document.getElementById("questions1").appendChild(j)
}
             
function num_questions2() {
    let style = "margin-top: 5px; margin-bottom: 10px"
    var q = 1
    let num = document.getElementById("hello2").value;
    let j = document.createElement("button");
    j.innerHTML = "Submit";
    j.setAttribute("onclick", "getData2();");

    for (let i = 0; i< num; i++){ 
        let dad = document.getElementById("questions2");
            
        let i = document.createElement("input");
        
                
        let apple = document.createTextNode("Question #" + q + " Answer Here: ");
        let k = document.createElement("br");
            
        i.innerHTML = "ko";
        
        i.setAttribute("class", "second-input")
                
        i.style = style
        dad.appendChild(k);
        dad.appendChild(apple);
        dad.appendChild(i);
        dad.appendChild(j);
        dad.appendChild(k);
        dad.appendChild(k);
        dad.appendChild(k);
        
        q++

    }

    document.getElementById("questions2").appendChild(j)
}

function num_questions3() {
    let style = "margin-top: 5px; margin-bottom: 10px"
    var q = 1
    let num = document.getElementById("hello3").value;
    let j = document.createElement("button");
    j.innerHTML = "Submit";
    j.setAttribute("onclick", "getData3();");

    for (let i = 0; i< num; i++){ 
        let dad = document.getElementById("questions3");
            
        let i = document.createElement("input");
        
                
        let apple = document.createTextNode("Question #" + q + " Answer Here: ");
        let k = document.createElement("br");
            
        i.innerHTML = "ko";

        i.setAttribute("class", "third-input")

                
        i.style = style
        dad.appendChild(k);
        dad.appendChild(apple);
        dad.appendChild(i);
        dad.appendChild(j);
        dad.appendChild(k);
        dad.appendChild(k);
        dad.appendChild(k);
        
        q++
    }
    document.getElementById("questions3").appendChild(j)
}

// Makes the button disappear after the user has clicked Submit on that button
function showStuff(){

  document.getElementById("holder").style.display = "none"
  document.getElementById("uploader").style.display = "block"

// Makes the Upload Image button disappear after the user has clicked the Upload Image button 
}

function showsub(){
  document.getElementById("uploader").style.display = "none"
  document.getElementById("subb").style.display = "block"

}

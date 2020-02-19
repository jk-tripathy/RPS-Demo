var { PythonShell } = require("python-shell")
var path = require("path")
var model_path = "../engine/rps3_2.h5"

var c_move = 'R'
var p_move = ''
var x_temp = []
var flag = 0
var p_score = 0
var c_score = 0

var to_num = { 'R': 1, 'P': 2, 'S': 3 }

function check(){
    if(p_move == "R"){
        if(c_move=="P"){
            c_score += 1
            flag += 1
        } else if(c_move=="S"){
            p_score += 1
            flag = 0
        } else if(c_move=="R"){
            flag += 1
        }
    }
    if (p_move == "P") {
        if (c_move == "S") {
            c_score += 1
            flag += 1
        } else if (c_move == "R") {
            p_score += 1
            flag = 0
        } else if (c_move == "P") {
            flag += 1
        }
    }
    if (p_move == "S") {
        if (c_move == "R") {
            c_score += 1
            flag += 1
        } else if (c_move == "P") {
            p_score += 1
            flag = 0
        } else if (c_move == "S") {
            flag += 1
        }
    }
}

function get_pred() {
    if(flag>=4){
        x_temp = []
    }
    if(x_temp.length > 18){
        x_temp.pop(0)
        x_temp.pop(0)
    }
    x_temp.push(to_num[p_move])
    x_temp.push(to_num[c_move])
    console.log(x_temp)
    var options = {
        scriptPath: path.join(__dirname, '/../engine/'),
        args: [model_path, x_temp]
    }
    let pyshell = new PythonShell('inference.py', options);
    pyshell.on('message', function (message) {
        console.log(message)
        c_move = message
    })

}

var p_score_id = document.getElementById("p_score")
var c_score_id = document.getElementById("c_score")

function highlight_comp(){
    if(c_move=="R"){
        c_r.src = "assets/rock.jpg";
        c_p.src = "assets/paper_bw.jpg";
        c_s.src = "assets/sci_bw.jpg";
    }else if(c_move=="P"){
        c_r.src = "assets/rock_bw.jpg";
        c_p.src = "assets/paper.jpg";
        c_s.src = "assets/sci_bw.jpg";
    }else{
        c_r.src = "assets/rock_bw.jpg";
        c_p.src = "assets/paper_bw.jpg";
        c_s.src = "assets/sci.jpg";
    }
    p_score_id.innerHTML = p_score
    c_score_id.innerHTML = c_score
}

var c_r = document.getElementById("c_r");
var c_p = document.getElementById("c_p");
var c_s = document.getElementById("c_s");


var p_r = document.getElementById("p_r");
p_r.onclick = function () {
    p_move = "R"
    check()
    highlight_comp()
    get_pred();
    console.log("Player:%s\tComputer:%s", p_score, c_score)
}

var p_p = document.getElementById("p_p");
p_p.onclick = function () {
    p_move = "P"
    check()
    highlight_comp()
    get_pred();
    console.log("Player:%s\tComputer:%s", p_score, c_score)
}

var p_s = document.getElementById("p_s");
p_s.onclick = function () {
    p_move = "S"
    check()
    highlight_comp()
    get_pred();
    console.log("Player:%s\tComputer:%s", p_score, c_score)
}

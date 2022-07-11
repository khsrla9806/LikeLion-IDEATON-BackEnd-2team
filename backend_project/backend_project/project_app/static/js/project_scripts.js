/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

const add_textbox = () => {
    const box = document.getElementById("box");
    const newP = document.createElement('p');
    newP.innerHTML = "<br/>일정: <input type='text' class='form-control' name='seqence []'> 장소: <input type='text' class='form-control' name='input[]'> 내용: <input type='text' class='form-control' name='input[]'><input type='button' value='삭제' onclick='remove(this)'>";
    box.appendChild(newP);
}
const remove = (obj) => {
    document.getElementById('box').removeChild(obj.parentNode);
}
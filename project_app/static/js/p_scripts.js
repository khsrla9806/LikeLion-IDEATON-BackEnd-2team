/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

const add_textbox = () => {
    const box = document.getElementById("box");
    let div = document.createElement('div');
    div.className = 'form-group is-valid';
    div.innerHTML = "<label for='id_sequence'>일정 순서</label><input type='text' name='sequence' class='form-control is-valid' placeholder='' title='' id='id_sequence'>\
    <label for='id_place'>장소</label><input type='text' name='place' class='form-control is-valid' placeholder='' maxlength='20' title='' id='id_place'>\
    <label for='id_detail_content'>세부 내용</label><textarea name='detail_content' cols='40' rows='10' class='form-control is-valid' placeholder='' maxlength='200' title='' id='id_detail_content'></textarea><input type='button' value='삭제' onclick='remove(this)'></input>";
    box.appendChild(div);
}
const remove = (obj) => {
    document.getElementById('box').removeChild(obj.parentNode);
}
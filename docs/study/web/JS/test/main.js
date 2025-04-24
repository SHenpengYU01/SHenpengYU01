const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');


let storyText = "今天气温 34 摄氏度，:inserta:出去遛弯。当走到:insertb:门前时，突然就:insertc:。人们都惊呆了，李雷全程目睹但并没有慌，因为:inserta:是一个 140 公斤的胖子，天气又辣么热。";
let insertX = `怪兽威利
大老爹
圣诞老人`;
insertX=insertX.split("\n");

let insertY = `肯德基
迪士尼乐园
白宫`;
insertY=insertY.split("\n");

let insertZ = `自燃了
在人行道化成了一坨泥
变成一条鼻涕虫爬走了`;
insertZ=insertZ.split("\n");

function randomValueFromArray(array) {
  return array[Math.floor(Math.random() * array.length)];
}



randomize.addEventListener('click', result);

function result() {
    let newStory = storyText;
    let XItem = randomValueFromArray(insertX);
    let YItem = randomValueFromArray(insertY);
    let ZItem = randomValueFromArray(insertZ);
    newStory = newStory.replaceAll(":inserta:",XItem);
    // newStory = newStory.replace(":inserta:",XItem);
    newStory = newStory.replace(":insertb:",YItem);
    newStory = newStory.replace(":insertc:",ZItem);


  if(customName.value !== '') {
    let name = customName.value;
    newStory = newStory.replace("李雷",name);
  }

  if(document.getElementById("american").checked) {
    let weight = Math.round(300*2.2) + " 磅";
    let temperature = Math.round(94*9/5+32)+ " 华氏度";
    newStory.replace("气温",temperature);
    newStory.replace("140 公斤",weight);
  }

  story.textContent = newStory;
  story.style.visibility = 'visible';
}
const audio = document.getElementById("audio");
const playBtn = document.getElementById("play");

playBtn.addEventListener('click', () => {
    if(audio.paused){
        audio.play();
        playBtn.innerText = '❚❚';
    } else {
        audio.pause();
        playBtn.innerText = '▶';
    }
});

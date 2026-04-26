const audio = document.getElementById("audio");
const playBtn = document.getElementById("play");
const progressContainer = document.getElementById('progress-container');
const progress = document.getElementById("progress");
const nextBtn = document.getElementById("next");
const prevBtn = document.getElementById("prev");
const title = document.querySelector(".titleMusic");


audio.addEventListener('timeupdate', () => {
    if(audio.duration){
        const margin = (audio.currentTime / audio.duration) * 100;
        progress.style.width = `${margin}%`;
    }
});

progressContainer.addEventListener("click", (e) => {
    const width = progressContainer.clientWidth;
    const clickX = e.offsetX;
    const duration = audio.duration;

    audio.currentTime = (clickX / width) * duration;
});

playBtn.addEventListener('click', () => {
    if(audio.paused){
        audio.play();
        playBtn.innerText = '❚❚';
    } else {
        audio.pause();
        playBtn.innerText = '▶';
    }
});

audio.addEventListener("ended", () => {
    playBtn.innerText = "▶";
});


const canciones = [
    {
        src: "../El Incidente de God Valley  SoulRap.mp3",
        titulo: "El Incidente de God Valley"
    },
    {
        src: "../Los Hermanos  Hola Soy German.mp3",
        titulo: "Hola Soy German"
    },
    {
        src: "../Nostálgico Amor - Nyako ft. KballeroRap (Prod. by Jose Delart)  Kowloon Generic Romance.mp3",
        titulo: "Nostálgico Amor"
    }
];

let indiceActual = 0;

function cargarCancion(indice) {
    audio.src = canciones[indice].src;
    title.innerText = canciones[indice].titulo;
    audio.play();
    playBtn.innerText = '❚❚';
}

nextBtn.addEventListener('click', () => {
    indiceActual++;
    
    if (indiceActual >= canciones.length) {
        indiceActual = 0;
    }
    
    cargarCancion(indiceActual);
});

prevBtn.addEventListener('click', () => {
    indiceActual--;
    
    if (indiceActual < 0) {
        indiceActual = canciones.length - 1;
    }
    
    cargarCancion(indiceActual);
});

function inicializarReproductor() {
    audio.src = canciones[indiceActual].src;
    title.innerText = canciones[indiceActual].titulo;
}

inicializarReproductor();
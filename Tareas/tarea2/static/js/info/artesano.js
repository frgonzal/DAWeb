let container = document.getElementById("container");
let small = document.getElementById("small_file");
let large = document.getElementById("large_file")

const increaseSize = () => {
    container.style.display = "none";
    large.style.display  = "flex"; 
};

const reduceSize = () => {
    container.style.display = "flex";
    large.style.display = "none";
};

small.addEventListener("click", increaseSize);
large.addEventListener("click", reduceSize  );



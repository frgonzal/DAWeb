let grafico1 = document.getElementById("grafico1");

let populateGraph = (data) => {
    while (grafico1.firstChild)
        grafico1.removeChild(grafico1.firstChild);

    for (info of data) {
        let option = document.createElement("p");
        option.innerText = info;
        grafico1.append(option);
    }
};

let fetchAJAX = (url) => {
    fetch(url) // 1 acceder al url
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json(); // 2 parseamos el response a un json
        })
        .then((ajaxResponse) => {
            populateGraph(ajaxResponse["data"]); // 3 le pasamos el data a populate...()
        })
        .catch((error) => {
            console.error(
                "There has been a problem with your fetch operation:",
                error
            );
        });
};

setInterval(handleAJAX => {
    fetchAJAX(url_grafico_artesanos);
    console.log("hola");
}, 2000);
fetchAJAX(url_grafico_hinchas);
const populateGraph = (id_graph, title, yLabel, animation, categories, data) => {
    Highcharts.chart(id_graph, {
        chart: {
            type: 'bar'
        },
        title: {
            text: title,
            align: 'left'
        },
        xAxis: {
            categories: categories,
            title: {
                text: "Categorías"
            },
            gridLineWidth: 0,
            lineWidth: 2,
        },
        yAxis: {
            min: 0,
            title: {
                text: yLabel,
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            },
            gridLineWidth: 1,
            lineWidth: 2
        },
        plotOptions: {
            bar: {
                color: '#009999',
                animation: animation,
                borderRadius: '25%',
                dataLabels: {
                    enabled: true
                },
                groupPadding: 0,
            }
        },
        legend: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        series: [{
            name:'',
            data: data,
        }]
    });
};

let fetchAJAX = (id_graph, title, yLabel, animation, url) => {
    fetch(url)
        .then((response) => {
            if (!response.ok)
                throw new Error("Network response was not ok");
            return response.json();
        })
        .then((ajaxResponse) => {
            populateGraph(id_graph, title, yLabel, animation,
                ajaxResponse["data"]["categories"], ajaxResponse["data"]["data"]);
        })
        .catch((error) => {
            console.error(
                "There has been a problem with your fetch operation:",
                error
            );
        });
};

setInterval(handleAJAX => {
    fetchAJAX('grafico_hinchas', 'Estadísticas Hinchas', 'Hinchas por Deporte', false, url_grafico_hinchas);
    fetchAJAX('grafico_artesanos', 'Estadísticas Artesanos', 'Artesanos por Artesanía', false, url_grafico_artesanos);
}, 2000);
fetchAJAX('grafico_artesanos', 'Estadísticas Artesanos', 'Artesanos por Artesanía', true, url_grafico_artesanos);
fetchAJAX('grafico_hinchas', 'Estadísticas Hinchas', 'Hinchas por Deporte', true, url_grafico_hinchas);



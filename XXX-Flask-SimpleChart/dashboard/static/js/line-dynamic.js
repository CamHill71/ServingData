var lineChartCanvas1 = document.getElementById('line-dynamic')
var lineData = {
    datasets: [
        {
            label: 'Data',
            line: '',
            data: [0],
            borderWidth: 2,
            lineTension: 0.2,
            fill: false,
            borderColor: [
                'rgba(128, 64, 65, 1)',
            ],
        },
    ],
}

var lineOptions = {
    legend: {display: false},
    title: {
        display: true,
        text: 'CPU Load'
    },
    scales: {
        xAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Time',
            },
        }],
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Percentage',
            },
            ticks: {
                beginAtZero: true,
                suggestedMin: 0,
                suggestedMax: 100,
            },
        }],
    },
}

var myRandomLineChart = new Chart(lineChartCanvas1, {
    type: 'line',
    data: lineData,
    options: lineOptions,
})

var z = new Ziggurat();

var counter = 0
var lineRandomUpdate = function () {
    var randomData = clamp(z.nextGaussian()*5,-5,10)
    myRandomLineChart.data.labels.push(counter)
    myRandomLineChart.data.datasets[0].data.push(randomData)
    if (counter > 25) {
        myRandomLineChart.data.labels.shift()
        myRandomLineChart.data.datasets[0].data.shift()
    }
    myRandomLineChart.update()
    counter++
}

setInterval(lineRandomUpdate, 1000);
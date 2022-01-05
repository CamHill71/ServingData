var barChartCanvas1 = document.getElementById('bar-random')
var barData = {
    labels: ['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape'],
    datasets: [{
        label: 'Popularity',
        data: [0, 0, 0, 0, 0, 0],
        borderWidth: 1,
        backgroundColor: [
            'rgba(160, 221, 90, 0.4)',
            'rgba(252, 205, 67, 0.4)',
            'rgba(192, 0, 0, 0.4)',
            'rgba(146, 72, 44, 0.4)',
            'rgba(101, 110, 5, 0.4)',
            'rgba(111, 45, 168, 0.4)',
        ],
        borderColor: [
            'rgba(160, 221, 90, 1)',
            'rgba(252, 205, 67, 1)',
            'rgba(192, 0, 0, 1)',
            'rgba(146, 72, 44, 1)',
            'rgba(101, 110, 5, 1)',
            'rgba(111, 45, 168, 1)',
        ],
    }],
}

var barOptions = {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
            },
        }],
    },
}

var myBarChart1 = new Chart(barChartCanvas1, {
    type: 'bar',
    data: barData,
    options: barOptions,
})

var barRandomUpdate = function () {

    var randomData = []
    for (count = 0; count < 6; count++) {
        randomData.push(getRandomIntInclusive(0, 20))
    }

    myBarChart1.data.datasets[0].data =randomData
    myBarChart1.update()
}

setInterval(barRandomUpdate, 1000);
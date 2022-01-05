var chartCanvas1 = document.getElementById('static-chart')
var barData = {
    labels: ['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape'],
    datasets: [{
        label: 'Popularity',
        data: [12, 5, 8, 23, 17, 6],
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

var myChart1 = new Chart(chartCanvas1, {
    type: 'bar',
    data: barData,
    options: barOptions,
})
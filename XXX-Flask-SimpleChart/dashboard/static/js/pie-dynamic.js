var pieChartCanvas2 = document.getElementById('pie-dynamic')
var pieData = {
    labels: ['CPU Use', 'Idle'],
    datasets: [{
        data: [0, 100],
        borderWidth: 1,
        borderAlign: 'inner',
        backgroundColor: [
            'rgba(192, 0, 0, 0.4)',
            'rgba(64, 64, 192, 0.4)',
        ],
        borderColor: [
            'rgba(192, 0, 0, 1)',
            'rgba(64, 64, 192, 1)',
        ],
    }],
}

var pieOptions = {}

var myPieChart = new Chart(pieChartCanvas2, {
    type: 'pie',
    data: pieData,
    options: pieOptions,
})

var pieRandomUpdate = function () {
    var currentCPU = myPieChart.data.datasets
    var newCPU = currentCPU[0].data[0] - getRandomIntInclusive(-5, 5)
    if (newCPU > 100) {
        newCPU = 100
    } else {
        if (newCPU < 0) {
            newCPU = 0
        }
    }
    var newIdle = 100 - newCPU
    myPieChart.data.datasets[0].data = [newCPU, newIdle]
    myPieChart.update()
}

setInterval(pieRandomUpdate, 500);
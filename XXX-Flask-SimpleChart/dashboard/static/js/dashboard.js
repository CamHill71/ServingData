var chartCanvas2 = document.getElementById('chart-2')
var pieData = {
    labels: ['CPU Load', 'Idle'],
    datasets: [{
        label: '%age',
        data: [12, 88],
        borderWidth: 1,
        borderAlign: 'inner',
        backgroundColor: [
            'rgba(255, 99, 132, 0.4)',
            'rgba(0, 0, 0, 0.4)',
        ],
        borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(0, 0, 0, 1)',
        ],
    }],
}

var pieOptions = {
    responsive: true,
}

var myChart2 = new Chart(chartCanvas2, {
    type: 'pie',
    data: pieData,
    options: pieOptions,
})

const updatePie = CPUValue =>
    setTimeout(() => {
        myChart2.data[0].points[0].value = CPUValue
        myChart2.data[0].points[1].value = 100-CPUValue
        myChart2.update()
        updatePie(Math.random(100))
    }, 1000);
updatePie(0);
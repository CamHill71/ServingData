(function () {

    'use strict'
    const ctx = document.getElementById('moneyChart').getContext('2d');


    var lineData = {
        datasets: [{
            label: 'Holdings overall $gain/loss',
            line: '',
            data: [],
            borderWidth: 2,
            lineTension: 0.2,
            fill: false,
            borderColor: [
                'rgba(35, 115, 61, 1)',
            ],
        }, ],
    };


    let lineOptions = {
        type: 'line',
        responsive: true,
        legend: {
            display: true
        },
        title: {
            display: true,
            text: "CPU LOAD"
        },
        scales: {
            xAxes: {

                display: true,
                lablestring: "Time"
            },
            yAxes: {
                display: true,
                lablestring: "Percentage",
                beginAtZero: true,
                suggestedMin: -10,
                suggestedMax: 10

            }
        }
    };


    const myChart = new Chart(ctx, {
        type: 'line',
        data: lineData,
        options: lineOptions
    });

    var recurring_sum = 0.0;
    var last_sum = 0.0;

    for (let i = 0; i < resultList2.length; i++) {

        let new_string = resultList2[i];

        // label
        myChart.data.labels.push(new_string[0]);

        // recurring data       
        recurring_sum = (last_sum + parseFloat(new_string[1]));

        // data
        myChart.data.datasets[0].data.push(recurring_sum);
        myChart.update();

        last_sum = recurring_sum;

    }






















}())
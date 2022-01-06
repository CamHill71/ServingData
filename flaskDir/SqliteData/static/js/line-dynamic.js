(function () {
    "use strict"
    let lineChartCanvas1 = document.getElementById("line-dynamic");

    const labels = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
      ];
      const data = {
        labels: labels,
        datasets: [{
          label: 'My First dataset',
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          data: [0, 10, 5, 2, 20, 30, 45],
        }]
      };

      const config = {
        type: 'line',
        data: data,
        options: {}
      };

      const myChart = new Chart(
        document.getElementById('dynamic22'),
        config
      );
    

    /*
    let lineData = {        
        datasets: [{
            //label: "Data",
           // line: "",
           // data: [0],
            //borderwidth: 2,
            //lineTension: 0.2,
            //fill: false,
            //borderColor: ["rgba(128,64,65,1)",],
        }]
    };

    const data = {
        
        datasets: [
          {
            label: 'Dataset 1',
            data: [0],
            borderColor: ["rgba(128,64,65,1)",],
            backgroundColor: ["rgba(128,64,65,1)",],
          },

        ]
      };


    let lineOptions = {
        legend: {
            display: false  
        },
        title: {
            display: true,
            text: "CPU LOAD"
        },

        scales: {
            xAxes: {
                scalelabel: {
                    display: true,
                    lablestring: "Time"
                }
            },
            yAxes: {
                scalelabel: {
                    display: true,
                    lablestring: "Percentage"
                },
                ticks: {
                    beginAtZero: true,
                    suggestedMin: 0,
                    suggestedMax: 100
                }


            }
        }
    }

    let myDynamicLineChart = new Chart(lineChartCanvas1, {
        type: "line",   
        data: data,
        //options: lineOptions,
    })

    var counter = 0;

    let url = "http://127.0.0.1:5000/api/cpu-load/5"; //apps chart url
    let method = "GET";
    let typeOfResponse = "json";

    let xhr = new XMLHttpRequest();
    xhr.open(method, url, true);
    xhr.responseType = typeOfResponse;
    xhr.send();

    xhr.onload = function () {
        let responseObj = xhr.response

        for (let responseNumber in responseObj) {
            let response = responseObj[responseNumber];            

            myDynamicLineChart.data.labels.unshift(response.created_at);
            myDynamicLineChart.data.datasets[0].data.unshift(response.load);

            //myDynamicLineChart.update();

            counter++;
            console.log(counter)

            console.log(response.created_at)
            console.log(response.load)
        }
    } */

}())
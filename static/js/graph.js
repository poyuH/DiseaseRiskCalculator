function transformData(data, keyY) {
    var new_data = [];
    console.log(data);

    for (i = 0; i < data['date'].length; i++) {
        new_data.push(
            {x: new Date(data['date'][i]), y: data[keyY][i]},
        );
    };
    return(new_data);
};

function drawLineChart(ctx, data, label, chartType) {
// data and label are nested arrays
var backgroundColor = 'rgba(153, 102, 200, 0.2)';
var borderColor = 'rgba(153, 102, 200, 1)';
if (chartType == 'BMI') {
    var dataSets = [{
        label: label[0],
        data: data[0],
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
    }]
}
if (chartType == 'BP'){
    var dataSets = [{
        label: label[0],
        data: data[0],
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
    },{
        label: label[1],
        data: data[1],
        backgroundColor: 'rgba(75, 192, 10, 0.2)',
        borderColor: 'rgba(75, 192, 10, 1)',
        borderWidth: 1
    }]
}

var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: dataSets,
    },
    options: {
        scales: {
            xAxes: [{
                type: 'time',
                ticks: {
                    source: 'data',
                },
                time: {
                    displayFormats: {
                        day: 'MM/DD/YYYY'
                    },
                    unit: 'day',
                }
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
};


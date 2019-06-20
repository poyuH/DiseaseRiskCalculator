$.fn.greenify = function() {
    this.css( "color", "green" );
};

function transformData(data, keyY) {
    var new_data = [];

    for (i = 0; i < data['date'].length; i++) {
        new_data.push(
            {x: new Date(data['date'][i]), y: data[keyY][i]}
        );
    };
    return(new_data);
};

function drawLineChart(ctx, data, label) {
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: label,
            data: data,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'day'
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


//function lineChart(result){


var ctx = document.getElementById("productsChart");


var datas = context.datas;
var mini_me = context.mini_me;
var essenza = context.essenza;
var inissia = context.inissia;
var mimo_cafeteira = context.mimo_cafeteira;
var pop_plus = context.pop_plus;

var productsChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: datas,
        datasets: [

        {
          label: 'Mini Me',
          data: mini_me,
          backgroundColor: 'rgba(0, 0, 0, 0)' ,
          borderColor: 'rgba(0,0,0, 0.9)' ,
//          borderWidth: 1
        },
        {
          label: 'Essenza',
          data: essenza,
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(255,99,132,1)',
//          borderWidth: 1
        },
        {
          label: 'Inissia',
          data: inissia,
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(54, 162, 235, 1)',
//          borderWidth: 1
        },
        {
          label: 'Mimo Cafeteira',
          data: mimo_cafeteira,
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(255, 206, 86, 1)',
//          borderWidth: 1
        },
        {
          label: 'Pop Plus',
          data: pop_plus,
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(75, 192, 192, 1)',
//          borderWidth: 1
        }

        ]
    },
  options: {

        responsive: true,
        title: {
            display: true,
            text: 'Evolução de Preço'
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Dia'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Preço'
                }
            }]
        }


  }
});



//}
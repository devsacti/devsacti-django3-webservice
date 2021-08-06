
    function display(datas){
//---------------------------------------------------------------------
Highcharts.chart('imper', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'PER of power stock'
    },
    subtitle: {
        text: 'Source: <a href="http://en.wikipedia.org/wiki/List_of_cities_proper_by_population">Wikipedia</a>'
    },
    xAxis: {
        type: 'category',
        labels: {
            rotation: -45,
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'PER atleast over then 50'
        }
    },
    legend: {
        enabled: false
    },
    tooltip: {
        pointFormat: 'Population in 2017: <b>{point.y:.1f} millions</b>'
    },
    series: [{
        name: 'Population',
        data: datas,
        dataLabels: {
            enabled: true,
            rotation: -90,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y:.1f}', // one decimal
            y: 10, // 10 pixels down from the top
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    }]
});
//---------------------------------------------------------------------
    };

    function getdata(){
        $.ajax({
            url:'js-dashboard4',
            datatype:'JSON',
            success:function(data){
                display(data);
                alert('check at success')
            }
        });
    };

    $(document).ready(function(){
        getdata();
    });
alert('check at dashboard4 javascript at static.js')
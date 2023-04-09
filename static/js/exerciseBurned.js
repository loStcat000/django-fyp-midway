var sodium = 0,
    potassium = 0,
    cholesterol = 0,
    dietaryfiber = 0,
    sugar = 0,
    iron = 0,
    magnesium = 0,
    calcium = 0;

var sodiumValue = document.getElementById('sodium_details').value;
sodium = parseFloat(sodiumValue);

var potassiumValue = document.getElementById('potassium_details').value;
potassium = parseFloat(potassiumValue);

var cholesterolValue = document.getElementById('cholesterol_details').value;
cholesterol = parseFloat(cholesterolValue);

var DietaryfiberValue = document.getElementById('Dietaryfiber_details').value;
dietaryfiber = parseFloat(DietaryfiberValue);

var sugarValue = document.getElementById('Sugar_details').value;
sugar = parseFloat(sugarValue);

var ironValue = document.getElementById('Iron_details').value;
iron = parseFloat(ironValue);

var magnesiumValue = document.getElementById('Magnesium_details').value;
magnesium = parseFloat(magnesiumValue);

var calciumValue = document.getElementById('Calcium_details').value;
calcium = parseFloat(magnesiumValue);

var ctx = document.getElementById('microChart');
var microChart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: [
            'sodium',
            'potassium',
            'cholesterol',
            'dietaryfiber',
            'sugar',
            'iron',
            'magnesium',
            'calcium',

        ],
        datasets: [{


            data: [sodium, potassium, cholesterol, dietaryfiber, sugar, iron, magnesium, calcium],
            backgroundColor: ['#e5a641', ],
        }],
    },
    options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: true,


        animation: {
            animateScale: true,
        },
        plugins: {
            legend: {
                display: true,
                position: 'bottom',
            },
            title: {
                display: true,
                text: 'Macronutrients Breakdown',
                font: {
                    size: 20,
                },
            },
            datalabels: {
                display: true,
                color: '#fff',
                font: {
                    weight: 'bold',
                    size: 16,
                },
                textAlign: 'center',
            },
        },
    },
});
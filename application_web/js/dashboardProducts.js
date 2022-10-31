//Test d'affichage dynamique de résultats
var chartLabels = [];
var chartData = [];


//Recuperation du contenu du fichier JSON
fetch('../../simulation_reseau/test.json')
    .then((response) => response.json())
    .then((json) => {
        listeEntreprises = json['reponse']['liste_entreprises'];
        id_requete = json['reponse']['id_discussion']
        
        for (i in listeEntreprises) {
            chartLabels.push(listeEntreprises[i]);
        }
    });



//Creation des tableaux pour le graphique

var tempData = []

//Lecture du fichier json 

tempData.push(30);


tempData.push(60);


tempData.push(10);


const data = {
    labels : chartLabels,
    datasets: [{
        label: 'My First Dataset',
        data: tempData,
        backgroundColor: [
            '#04EDD2',
            '#A0CFD3',
            '#0D94BA',
            '#0A7AA0'
        ],
        borderColor: '#1E2019',
        borderRadius: 10,
        offset : 10,
        hoverOffset: 30
  }]
};

const config = {
    type: 'doughnut',
    data: data,
    options: {
        responsive: true,
        maintainAspectRatio : true,
        layout: {
            padding : 100
        },
    }
};

const myChart = new Chart(document.getElementById('myChart'), config);
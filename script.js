document.getElementById('forecastForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const location = document.getElementById('location').value;
    
    if (location.trim() === '') {
        alert('Please enter a location!');
        return;
    }

    fetch('/api/get_forecast', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ location: location }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('forecastResult').classList.remove('hidden');
        document.getElementById('forecastOutput').innerHTML = `For ${location}, we predict ${data.energy} kWh of solar energy tomorrow. We recommend using battery storage during ${data.optimal_hours}.`;

        // Chart can be generated here
        generateChart(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function generateChart(data) {
    const ctx = document.getElementById('forecastChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.hours,
            datasets: [{
                label: 'Energy (kWh)',
                data: data.energy_per_hour,
                borderColor: 'rgba(75, 192, 192, 1)',
                fill: false,
            }]
        }
    });
}

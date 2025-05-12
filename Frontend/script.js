
const apiKey = 'fda9555743ded8c01a764b5822478dc8';


function getWeather() {
  const city = document.getElementById('cityInput').value;
  fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
    .then(res => res.json())
    .then(data => {
      const display = document.getElementById('weatherDisplay');
      display.innerHTML = `
        <p><strong>Temperature:</strong> ${data.main.temp} °C</p>
        <p><strong>Humidity:</strong> ${data.main.humidity} %</p>
        <p><strong>Condition:</strong> ${data.weather[0].description}</p>
      `;
    })
    .catch(err => {
      console.error(err);
      alert('Weather fetch failed. Please check your API key or city name.');
    });
}


// Simulate sensor data every 3 seconds
setInterval(() => {
  document.getElementById('temp').innerText = (20 + Math.random() * 10).toFixed(1);
  document.getElementById('moisture').innerText = (40 + Math.random() * 30).toFixed(0);
  document.getElementById('humidity').innerText = (50 + Math.random() * 30).toFixed(0);
}, 3000);



// Crop Health Analytics - mock data
const ctx = document.getElementById('healthChart').getContext('2d');
const healthChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Today'],
    datasets: [{
      label: 'Crop Health Index',
      data: [60, 65, 70, 75, 80],
      borderColor: 'green',
      fill: false
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: { beginAtZero: true, max: 100 }
    }
  }
});

// Pest Detection Upload
document.getElementById('pestForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const fileInput = document.getElementById('imageInput');
  const file = fileInput.files[0];

  if (!file) {
    alert('Please select an image');
    return;
  }

  const formData = new FormData();
  formData.append('image', file);

  fetch('http://127.0.0.1:5000/upload-pest-image', {
    method: 'POST',
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('pestResult').innerText = data.result || data.error;
  })
  .catch(err => {
    console.error('Upload failed:', err);
    alert('Upload failed');
  });
});




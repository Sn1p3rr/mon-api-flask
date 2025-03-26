document.addEventListener("DOMContentLoaded", function () {
  fetch('https://mon-api-flask.onrender.com/api/deals')
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById('deals-container');
      data.forEach(deal => {
        container.innerHTML += `
          <div class="deal">
            <h3>${deal.nom}</h3>
            <p>${deal.prix}</p>
            <a href="${deal.url}" target="_blank">Voir l'offre</a>
          </div>`;
      });
    })
    .catch(err => {
      document.getElementById('deals-container').innerHTML = "<p>Erreur lors du chargement des deals 😥</p>";
      console.error("Erreur API:", err);
    });
});

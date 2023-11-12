fetch("http://127.0.0.1:8000/course/get_data")
  .then((res) => res.json())
  .then((data) => {
    data.forEach((member, rank) => {
      let newRow = document.createElement("li");
      newRow.classList = "c-list__item";
      newRow.innerHTML = `
			  <div class="c-list__grid">
				  <div class="c-flag c-place u-bg--transparent">${rank+1}</div>
				  <div class="c-media">
					  <img class="c-avatar c-media__img" src="${member.image}" />
					  <div class="c-media__content">
						  <div class="c-media__title">${member.username}</div>
					  </div>
				  </div>
				  <div class="u-text--right c-kudos">
					  <div class="u-mt--8">
						  <strong>${member.earned}</strong>
					  </div>
				  </div>
			  </div>
		  `;
      if (rank+1 === 1) {
        newRow.querySelector(".c-place").classList.add("u-text--dark");
        newRow.querySelector(".c-place").classList.add("u-bg--yellow");
        newRow.querySelector(".c-kudos").classList.add("u-text--yellow");
      } else if (rank+1 === 2) {
        newRow.querySelector(".c-place").classList.add("u-text--dark");
        newRow.querySelector(".c-place").classList.add("u-bg--teal");
        newRow.querySelector(".c-kudos").classList.add("u-text--teal");
      } else if (rank+1 === 3) {
        newRow.querySelector(".c-place").classList.add("u-text--dark");
        newRow.querySelector(".c-place").classList.add("u-bg--orange");
        newRow.querySelector(".c-kudos").classList.add("u-text--orange");
      }
      list.appendChild(newRow);
    });

    // Find Winner from sent kudos by sorting the drivers in the team array
    let sortedTeam = data.sort((a, b) => b.sent - a.sent);
    let winner = sortedTeam[0];

    // Render winner card
    const winnerCard = document.getElementById("winner");
    winnerCard.innerHTML = `
		  <div class="u-text-small u-text--medium u-mb--16">Top Sender Last Week</div>
		  <img class="c-avatar c-avatar--lg" src="${winner.image}"/>
		  <h3 class="u-mt--16">${winner.username}</h3>
		  <span class="u-text--teal u-text--small">${winner.username}</span>
	  `;
  });

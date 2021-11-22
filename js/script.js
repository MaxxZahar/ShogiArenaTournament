let results, players;
Promise.all([
    fetch('../php/getPlayers.php')
        .then(response => response.json()),
    fetch('../php/getResults.php')
        .then(response => response.json())
]).then(jsons => console.log(dataProcessing(jsons[0], jsons[1])));

function dataProcessing(players, results) {
    console.log(players);
    console.log(results);
    const numberOfPlayers = players.length;
    const numberOfGames = results.length;
    const points = Array(numberOfPlayers).fill(0);
    const gamesPlayed = Array(numberOfPlayers).fill(0);
    for (let i = 0; i < numberOfGames; i++) {
        points[Number(results[i].winner) - 1]++;
        gamesPlayed[Number(results[i].winner) - 1]++;
        gamesPlayed[Number(results[i].loser) - 1]++;
    }
    players.forEach((player, i) => { player['points'] = points[i]; player['winRate'] = points[i] / gamesPlayed[i]; player['games'] = [] });
    players.sort((a, b) => {
        if (b.points - a.points) return b.points - a.points;
        return b.winRate - a.winRate});
    for (let i = 0; i < numberOfGames; i++) {
        const winnerID = results[i].winner;
        const loserID = results[i].loser;
        const winnerIndex = players.findIndex(player => player.id == winnerID);
        const loserIndex = players.findIndex(player => player.id == loserID);
        if (players[winnerIndex].games.length === players[loserIndex].games.length){
            addResult(players, winnerIndex, loserIndex);
        } else if (players[winnerIndex].games.length > players[loserIndex].games.length){
            const diff = players[winnerIndex].games.length - players[loserIndex].games.length;
            for (let j = 0; j < diff; j++){
                players[loserIndex].games.push('0-');
            }
            addResult(players, winnerIndex, loserIndex);
        } else {
            const diff = players[loserIndex].games.length - players[winnerIndex].games.length;
            for (let j = 0; j < diff; j++){
                players[winnerIndex].games.push('0-');
            }
            addResult(players, winnerIndex, loserIndex);
        }
    }
    let maxLength = 0;
    for (let j = 0; j < numberOfPlayers; j++){
        if (players[j].games.length > maxLength){
            maxLength = players[j].games.length;
        }
    }
    for (let j = 0; j < numberOfPlayers; j++){
        if (maxLength > players[j].games.length){
            const diff = maxLength - players[j].games.length;
            for (let k = 0; k < diff; k++){
                players[j].games.push('0-');
            }
        }
    }
    let table = "";
    for (let j = 0; j < numberOfPlayers; j++){
        table += `${j + 1} [${players[j].surname}] [${players[j].name}] [${gamesToString(players[j].games)}] ${players[j].points} \n`;
    }
    const input = document.querySelector('input[type="hidden"]');
    input.value = table;
    return table;
}

function addResult(players, winnerIndex, loserIndex){
    players[winnerIndex].games.push(`${loserIndex + 1}+`);
    players[loserIndex].games.push(`${winnerIndex + 1}-`);
}

function gamesToString(games){
    return games.reduce((acc, el) => acc + ' ' + el);
}
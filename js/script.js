let results, players;
Promise.all([
    fetch('../php/getPlayers.php')
        .then(response => response.json()),
    fetch('../php/getResults.php')
        .then(response => response.json())        
]).then(jsons => console.log(dataProcessing(jsons[0], jsons[1])));

function dataProcessing(players, results){
    console.log(players);
    console.log(results);
    const numberOfPlayers = players.length;
    const numberOfGames = results.length;
    const points = Array(numberOfPlayers).fill(0);
    for (let i = 0; i < numberOfGames; i++){
        points[Number(results[i].winner) - 1]++;
    }
    players.forEach((player, i) => player['points'] = points[i]);
    players.sort((a, b) => b.points - a.points);
    for (let i = 0; i < numberOfGames; i++){
        const winnerID = results[i].winner;
        const loserID = results[i].loser;
        const winnerIndex = players.findIndex(player => player.id == winnerID);
        const loserIndex = players.findIndex(player => player.id == loserID);
        console.log(winnerIndex, loserIndex);
    }
    return points;
}

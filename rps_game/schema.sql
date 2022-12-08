DROP TABLE IF EXISTS rps_game;
DROP INDEX IF EXISTS rps_game_playerA;
DROP INDEX IF EXISTS rps_game_playerB;
DROP INDEX IF EXISTS rps_game_playerWinner;

/**
 * Given the requirements, a single table should be enough.
 * Treat the user provided names as unique identifiers.
 * Each row is a single game. Aggregate over the players to determine score.
 */
CREATE TABLE rps_game (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  playerA TEXT NOT NULL,
  playerB TEXT, -- null if computer player

  playerAMove TEXT, -- rock, paper, scissors
  playerBMove TEXT,

  playerWinner TEXT,

  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX rps_game_playerA ON rps_game(playerA);
CREATE INDEX rps_game_playerB ON rps_game(playerB);
CREATE INDEX rps_game_playerWinner ON rps_game(playerWinner);

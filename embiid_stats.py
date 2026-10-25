from nba_api.stats.endpoints import playercareerstats
import matplotlib.pyplot as plt

# Pull Joel Embiid's career stats
df = playercareerstats.PlayerCareerStats(player_id=203954).get_data_frames()[0]
df = df[df["SEASON_ID"] != "2026-27"]

# Per-game scoring and True Shooting %
df["PPG"] = df["PTS"] / df["GP"]
df["TS_PCT"] = df["PTS"] / (2 * (df["FGA"] + 0.44 * df["FTA"]))

# Games missed (2019-20 and 2020-21 were shortened seasons)
season_length = {"2019-20": 73, "2020-21": 72}
df["GAMES_MISSED"] = df["SEASON_ID"].map(season_length).fillna(82) - df["GP"]

print(df[["SEASON_ID", "GP", "GAMES_MISSED", "PPG", "TS_PCT"]])

# One figure, two charts
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
ax[0].plot(df["SEASON_ID"], df["PPG"], marker="o")
ax[0].set_title("Embiid: Points Per Game")
ax[1].bar(df["SEASON_ID"], df["GAMES_MISSED"], color="firebrick")
ax[1].set_title("Embiid: Games Missed")
for a in ax:
    a.tick_params(axis="x", rotation=45)
plt.tight_layout()
plt.savefig("embiid_summary.png")
plt.show()
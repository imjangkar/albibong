import AccessTimeIcon from "@mui/icons-material/AccessTime";
import { TextField, Typography } from "@mui/material";
import { useContext, useState } from "react";
import app from "../App.module.css";
import { formatter } from "../pages/DPSMeter";
import styles from "../pages/DungeonTracker.module.css";
import { WebsocketContext } from "../providers/WebsocketProvider";
import { Dungeon } from "../providers/WorldProvider";
import { theme } from "../theme";

type DungeonCardProps = {
  dungeon: Dungeon;
};

const DungeonCard = ({ dungeon }: DungeonCardProps) => {
  const { sendMessage } = useContext(WebsocketContext);

  const updateDungeonName = () => {
    sendMessage({
      type: "update_dungeon_name",
      payload: { id: dungeon.id, value: name },
    });
  };

  const updateTierDungeon = () => {
    sendMessage({
      type: "update_dungeon_tier",
      payload: { id: dungeon.id, value: tier },
    });
  };

  const [name, setName] = useState(dungeon.name);
  const [tier, setTier] = useState(String(dungeon.tier));

  return (
    <div
      className={styles.dungeonContainer}
      style={{ backgroundColor: theme.palette.background.paper }}
    >
      <div className={app.row}>
        <div className={styles.tag}>
          <Typography>{dungeon.type}</Typography>
        </div>
        <Typography>{dungeon.date_time}</Typography>
      </div>
      <div className={app.stats}>
        <TextField
          id={dungeon.id}
          variant="standard"
          sx={{ width: `${name.length * 1.5}ch` }}
          value={name}
          onBlur={updateDungeonName}
          onChange={(e) => setName(e.target.value)}
        />
        <Typography variant="h2"> • Tier</Typography>
        <TextField
          type="number"
          inputMode="numeric"
          id={dungeon.id}
          variant="standard"
          sx={{ width: "2ch" }}
          value={tier}
          onBlur={updateTierDungeon}
          onChange={(e) => setTier(e.target.value)}
        />
      </div>

      <div className={app.options}>
        <div className={app.stats}>
          <img src="fame.png" width={"24px"} />
          <Typography>{formatter(Math.round(dungeon.fame))}</Typography>
        </div>
        <div className={app.stats}>
          <img src="silver.png" width={"24px"} />
          <Typography>{formatter(Math.round(dungeon.silver))}</Typography>
        </div>
        <div className={app.stats}>
          <img src="re_spec.png" width={"24px"} />
          <Typography>{formatter(Math.round(dungeon.re_spec))}</Typography>
        </div>
        <div className={app.stats}>
          <AccessTimeIcon />
          {dungeon.time_elapsed}
        </div>
      </div>
    </div>
  );
};

export default DungeonCard;

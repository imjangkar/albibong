import { Typography } from "@mui/material";
import app from "../App.module.css";
import dungeon from "../pages/DungeonTracker.module.css";
import styles from "../pages/FarmingTracker.module.css";
import { Island } from "../providers/WorldProvider";
import { theme } from "../theme";
import HarvestRow from "./HarvestRow";

type IslandCardProps = {
  island: Island;
};

const IslandCard = ({ island }: IslandCardProps) => {
  return (
    <div
      className={dungeon.dungeonContainer}
      style={{ backgroundColor: theme.palette.background.paper }}
    >
      <div className={app.row}>
        <Typography variant="h2">{island.name}</Typography>
        <Typography>{island.date_time}</Typography>
      </div>
      <div className={styles.row}>
        <div className={styles.column}>
          <Typography variant="h3">Crops</Typography>
          <HarvestRow harvestables={island.crops} type="crop" />
        </div>
        <div className={styles.column}>
          <Typography variant="h3">Animals</Typography>
          <HarvestRow harvestables={island.animals} type="animal" />
        </div>
      </div>
    </div>
  );
};

export default IslandCard;

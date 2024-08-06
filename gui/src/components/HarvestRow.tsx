import { Typography } from "@mui/material";
import { formatter } from "../pages/DPSMeter";
import styles from "../pages/FarmingTracker.module.css";
import { Item } from "../providers/WorldProvider";

type HarvestRowProps = {
  harvestables: Item[];
  type: "crop" | "animal";
};

const HarvestRow = ({ harvestables, type }: HarvestRowProps) => {
  return (
    <>
      {harvestables.length > 0 ? (
        harvestables.map((harvest, index) => (
          <div className={styles.harvest} key={index}>
            <img width={"40px"} src={harvest.image} />
            <Typography style={{ width: "100%" }}>{harvest.name}</Typography>
            <Typography
              sx={{ fontWeight: "bold", width: "48px", textAlign: "right" }}
            >
              {formatter(harvest.quantity)}
            </Typography>
          </div>
        ))
      ) : (
        <Typography>No {type} harvested</Typography>
      )}
    </>
  );
};

export default HarvestRow;

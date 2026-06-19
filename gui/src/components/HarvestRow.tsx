import { Typography } from "@mui/material";
import { formatter } from "../pages/DPSMeter";
import styles from "../pages/FarmingTracker.module.css";
import { Item } from "../providers/WorldProvider";
import { useI18n } from "../providers/I18nProvider";

type HarvestRowProps = {
  harvestables: Item[];
  type: "crop" | "animal";
};

const HarvestRow = ({ harvestables, type }: HarvestRowProps) => {
  const { t } = useI18n();
  const noText = type === "crop" ? t("farming.noCropHarvested") : t("farming.noAnimalHarvested");

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
        <Typography>{noText}</Typography>
      )}
    </>
  );
};

export default HarvestRow;

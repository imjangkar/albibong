import { Typography } from "@mui/material";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import dayjs, { Dayjs } from "dayjs";
import "dayjs/locale/en-gb";

import { useContext, useEffect, useState } from "react";
import app from "../App.module.css";
import { WorldContext } from "../providers/WorldProvider";

import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers";
import HarvestRow from "../components/HarvestRow";
import IslandCard from "../components/IslandCard";
import { WebsocketContext } from "../providers/WebsocketProvider";
import { theme } from "../theme";
import styles from "./FarmingTracker.module.css";
import { useI18n } from "../providers/I18nProvider";

const FarmingTracker = () => {
  const { t } = useI18n();
  const { world, islandWidget } = useContext(WorldContext);
  const [dateRange, setDateRange] = useState<Dayjs>(dayjs(islandWidget.date));
  const { sendMessage } = useContext(WebsocketContext);

  const setDateForTotalHarvest = (value: any) => {
    setDateRange(value);

    const date = `${value.$y}-${value.$M + 1}-${value.$D}`;
    sendMessage({
      type: "update_total_harvested_date_range",
      payload: { date: date },
    });
  };

  useEffect(() => {
    setDateRange(dayjs(islandWidget.date));
  }, [islandWidget]);

  const date_to_string = () => {
    if (dateRange.isSame(dayjs(), "day") == true) {
      return t("farming.today");
    } else if (dateRange.isSame(dayjs().subtract(1, "day"), "day")) {
      return t("farming.yesterday");
    } else {
      return dateRange.format("dddd, D MMM").toString();
    }
  };

  return (
    <div className={app.container}>
      <Typography variant="h2">{t("farming.title")}</Typography>
      <div className={styles.statsContainer}>
        <div className={app.row}>
          <h2>{t("farming.totalHarvested", { date: date_to_string() })}</h2>
          <LocalizationProvider
            dateAdapter={AdapterDayjs}
            adapterLocale="en-gb"
          >
            <DatePicker
              slotProps={{ textField: { size: "small" } }}
              label={t("farming.dateRange")}
              value={dateRange}
              onChange={(newValue) => setDateForTotalHarvest(newValue)}
            />
          </LocalizationProvider>
        </div>
        <div className={styles.row}>
          <div className={styles.column}>
            <Typography variant="h3">{t("farming.crops")}</Typography>
            <HarvestRow harvestables={islandWidget.crops} type="crop" />
          </div>
          <div className={styles.column}>
            <Typography variant="h3">{t("farming.animals")}</Typography>
            <HarvestRow harvestables={islandWidget.animals} type="animal" />
          </div>
        </div>
      </div>
      <hr
        style={{
          width: "100%",
          borderColor: theme.palette.background.paper,
        }}
      />
      {world.list_island.map((island, index) => (
        <IslandCard island={island} key={index} />
      ))}
    </div>
  );
};

export default FarmingTracker;

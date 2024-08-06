import AccessTimeIcon from "@mui/icons-material/AccessTime";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";

import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  TextField,
  Typography,
} from "@mui/material";
import { useContext, useState } from "react";
import app from "../App.module.css";
import { formatter } from "../pages/DPSMeter";
import dps from "../pages/DPSMeter.module.css";
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

  const getMaxHeal = () => {
    let maxHeal = 0;
    dungeon.meter.forEach((member) => {
      if (member.healing_dealt > maxHeal) {
        maxHeal = member.healing_dealt;
      }
    });
    return maxHeal;
  };

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
      <Accordion style={{ marginTop: "1rem" }}>
        <AccordionSummary
          expandIcon={<ArrowDropDownIcon />}
          aria-controls="content"
          id="header"
        >
          <Typography variant="h4">Damage Meter Snapshot</Typography>
        </AccordionSummary>
        <AccordionDetails>
          {dungeon.meter.length > 0 ? (
            <>
              <Typography variant="h5">
                This is only a snapshot taken from <a href="/">Damage Meter</a>{" "}
                when the player left the dungeon. Results might be inaccurate if
                the meter didn't get reset after entering a new dungeon.
              </Typography>
              <br />
              <div className={dps.dpsRow}>
                <Typography className={dps.player}>Member</Typography>
                <Typography className={dps.dpsNumber}>Damage</Typography>
                <Typography className={dps.dpsNumber}>Damage%</Typography>
                <Typography className={dps.dpsNumber}>Duration</Typography>
                <Typography
                  className={dps.dpsNumber}
                  sx={{ fontWeight: "bold" }}
                >
                  DPS
                </Typography>
              </div>
            </>
          ) : null}
          {dungeon.meter.length > 0 ? (
            dungeon.meter.map((member, index) => {
              const pertama = dungeon.meter[0];
              const dpsPercent =
                member["damage_dealt"] / pertama["damage_dealt"];
              const dpsWidth = {
                width:
                  pertama["damage_dealt"] > 0 ? `${dpsPercent * 100}%` : "0",
              };
              const healPercent = member["healing_dealt"] / getMaxHeal();
              const healWidth = {
                width: getMaxHeal() > 0 ? `${healPercent * 100}%` : "0",
              };

              return (
                <div style={{ width: "100%" }} key={index}>
                  <div className={dps.dpsRow}>
                    <Typography style={{ marginRight: 16 }}>
                      {index + 1}.
                    </Typography>{" "}
                    <Typography className={dps.player}>
                      {member.username}
                    </Typography>
                    <img src={member.weapon} width={"48px"} height={"48px"} />
                    <Typography className={dps.dpsNumber}>
                      {formatter(member.damage_dealt)}
                    </Typography>
                    <Typography className={dps.dpsNumber}>
                      {formatter(member.damage_percent)}%
                    </Typography>
                    <Typography className={dps.dpsNumber}>
                      {member.combat_duration}
                    </Typography>
                    <Typography
                      className={dps.dpsNumber}
                      sx={{ fontWeight: "bold" }}
                    >
                      {member.dps}/dps
                    </Typography>
                  </div>
                  <div className={dps.dmgBar} style={dpsWidth} />
                  <div className={dps.healBar} style={healWidth} />
                </div>
              );
            })
          ) : (
            <Typography>No snapshot taken</Typography>
          )}
        </AccordionDetails>
      </Accordion>
    </div>
  );
};

export default DungeonCard;

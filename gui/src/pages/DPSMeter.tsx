import classNames from "classnames";
import { useContext, useRef, useState } from "react";
import styles from "./DPSMeter.module.css";
import dungeon from "./DungeonTracker.module.css";

import app from "../App.module.css";
import Checkbox from "../components/Checkbox";
import { WorldContext } from "../providers/WorldProvider";
import { WebsocketContext } from "../providers/WebsocketProvider";
import { Alert, Button, Collapse, Typography } from "@mui/material";
import {
  FiberManualRecord,
  Pause,
  ContentCopy,
  RestartAlt,
} from "@mui/icons-material";

import { theme } from "../theme";

export type DisplayedColumn = {
  Heal: boolean;
  Damage: boolean;
};

export const formatter = (num: number) => {
  return new Intl.NumberFormat("id").format(num);
};

const DPSMeter = () => {
  const [displayedCol, setDisplayedCol] = useState<DisplayedColumn>({
    Heal: false,
    Damage: true,
  });

  const [alert, setAlert] = useState({
    copyDamage: false,
    resetDamage: false,
    resetStats: false,
  });

  const dpsRef = useRef(null);

  const { me, world } = useContext(WorldContext);
  const { sendMessage } = useContext(WebsocketContext);

  const dpsRowBold = classNames(styles.bold, styles.dpsRow, dungeon.stickToTop);

  const getMaxHeal = () => {
    let maxHeal = 0;
    world.party.forEach((member) => {
      if (member.healing_dealt > maxHeal) {
        maxHeal = member.healing_dealt;
      }
    });
    return maxHeal;
  };

  const show = (label: keyof DisplayedColumn) =>
    classNames(styles.dpsNumber, {
      [styles.hidden]: !displayedCol[label],
    });

  const toggleRecord = (value: boolean) => {
    sendMessage({
      type: "update_is_dps_meter_running",
      payload: { value },
    });
  };

  const resetStats = () => {
    sendMessage({
      type: "reset_player_stats",
      payload: { value: true },
    });

    setAlert((prev) => ({ ...prev, resetStats: true }));
    setTimeout(() => {
      setAlert((prev) => ({ ...prev, resetStats: false }));
    }, 1000);
  };

  const resetDamage = () => {
    var partyMembers: string[] = [];
    world.party.forEach((member) => {
      partyMembers.push(member.username);
    });
    sendMessage({
      type: "reset_dps_meter",
      payload: { party_members: partyMembers },
    });
    setAlert((prev) => ({ ...prev, resetDamage: true }));
    setTimeout(() => {
      setAlert((prev) => ({ ...prev, resetDamage: false }));
    }, 1000);
  };

  const formatDamageToText = () => {
    var textToCopy = "";
    world.party.map((member, index) => {
      textToCopy += `${index + 1}.${member.username}: ${~~(
        member.damage_dealt / 1000
      )}K (${member.damage_percent}%) `;
    });
    navigator.clipboard.writeText(textToCopy);
    setAlert((prev) => ({ ...prev, copyDamage: true }));
    setTimeout(() => {
      setAlert((prev) => ({ ...prev, copyDamage: false }));
    }, 1000);
  };

  return (
    <div className={app.container}>
      <div className={app.snackbar}>
        <Collapse in={alert.copyDamage}>
          <Alert severity="success">Damage copied to clipboard.</Alert>
        </Collapse>
        <Collapse in={alert.resetDamage}>
          <Alert severity="success">Damage has been reset.</Alert>
        </Collapse>
        <Collapse in={alert.resetStats}>
          <Alert severity="success">Stats has been reset.</Alert>
        </Collapse>
      </div>
      <Typography variant="h2">Damage Meter</Typography>
      <Typography>
        Damage Meter is currently{" "}
        <b>{world.isDPSMeterRunning ? "recording damage" : "paused"}</b>
      </Typography>
      <div className={app.row}>
        <div className={app.options}>
          <div className={app.stats}>
            <img src="fame.png" width={"24px"} />
            <Typography>{formatter(Math.round(me.fame))}</Typography>
          </div>
          <div className={app.stats}>
            <img src="silver.png" width={"24px"} />
            <Typography>{formatter(Math.round(me.silver))}</Typography>
          </div>
          <div className={app.stats}>
            <img src="re_spec.png" width={"24px"} />
            <Typography>{formatter(Math.round(me.re_spec))}</Typography>
          </div>
        </div>
        <Button
          variant="text"
          startIcon={<RestartAlt />}
          onClick={() => resetStats()}
        >
          Reset Stats
        </Button>
      </div>
      <div className={app.row}>
        <div className={app.options}>
          <Checkbox
            label="Damage"
            checked={displayedCol.Damage}
            onclick={setDisplayedCol}
          ></Checkbox>
          <Checkbox
            label="Heal"
            checked={displayedCol.Heal}
            onclick={setDisplayedCol}
          ></Checkbox>
        </div>
        <Button
          variant="text"
          startIcon={<RestartAlt />}
          onClick={() => resetDamage()}
        >
          Reset Damage Meter
        </Button>
      </div>

      <div
        className={styles.dpsContainer}
        style={{ backgroundColor: theme.palette.background.default }}
        ref={dpsRef}
      >
        <div
          className={dpsRowBold}
          style={{ backgroundColor: theme.palette.background.default }}
        >
          <div className={styles.dpsButton}>
            {world.isDPSMeterRunning == false ? (
              <Button
                variant="outlined"
                startIcon={<FiberManualRecord />}
                onClick={() => toggleRecord(true)}
              >
                Record
              </Button>
            ) : (
              <Button
                variant="outlined"
                startIcon={<Pause />}
                onClick={() => toggleRecord(false)}
              >
                Pause
              </Button>
            )}
            <Button
              variant="contained"
              startIcon={<ContentCopy />}
              onClick={() => formatDamageToText()}
            >
              Copy Damage
            </Button>
          </div>

          <Typography className={show("Heal")}>Heal</Typography>
          <Typography className={show("Heal")}>Heal%</Typography>
          <Typography className={show("Damage")}>Damage</Typography>
          <Typography className={show("Damage")}>Damage%</Typography>
          <Typography className={styles.dpsNumber}>Duration</Typography>
          <Typography className={show("Damage")} sx={{ fontWeight: "bold" }}>
            DPS
          </Typography>
        </div>
        {world.party.map((member, index) => {
          const pertama = world.party[0];
          const dpsPercent = member["damage_dealt"] / pertama["damage_dealt"];
          const dpsWidth = {
            width: pertama["damage_dealt"] > 0 ? `${dpsPercent * 100}%` : "0",
          };
          const healPercent = member["healing_dealt"] / getMaxHeal();
          const healWidth = {
            width: getMaxHeal() > 0 ? `${healPercent * 100}%` : "0",
          };

          return (
            <div style={{ width: "100%" }} key={index}>
              <div className={styles.dpsRow}>
                <Typography style={{ marginRight: 16 }}>
                  {index + 1}.
                </Typography>{" "}
                <Typography className={styles.player}>
                  {member.username}
                </Typography>
                <img src={member.weapon} width={"48px"} height={"48px"} />
                <Typography className={show("Heal")}>
                  {member.healing_dealt > 0 && formatter(member.healing_dealt)}
                </Typography>
                <Typography className={show("Heal")}>
                  {member.heal_percent > 0 &&
                    `${formatter(member.heal_percent)}%`}
                </Typography>
                <Typography className={show("Damage")}>
                  {formatter(member.damage_dealt)}
                </Typography>
                <Typography className={show("Damage")}>
                  {formatter(member.damage_percent)}%
                </Typography>
                <Typography className={styles.dpsNumber}>
                  {member.combat_duration}
                </Typography>
                <Typography
                  className={show("Damage")}
                  sx={{ fontWeight: "bold" }}
                >
                  {member.dps}/dps
                </Typography>
              </div>
              <div className={styles.dmgBar} style={dpsWidth} />
              <div className={styles.healBar} style={healWidth} />
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default DPSMeter;

import { Dispatch, SetStateAction } from "react";
import { DisplayedColumn } from "../pages/DPSMeter";
import { Typography } from "@mui/material";
import app from "../App.module.css";
import { theme } from "../theme";
import { useI18n } from "../providers/I18nProvider";

type CheckboxProps = {
  label: keyof DisplayedColumn;
  required?: boolean;
  disabled?: boolean;
  checked: boolean;
  onclick: Dispatch<SetStateAction<DisplayedColumn>>;
};

const Checkbox = ({
  label,
  required = false,
  disabled = false,
  checked,
  onclick,
}: CheckboxProps) => {
  const { t } = useI18n();
  const labelKey = label === "Damage" ? "dps.damage" : "dps.heal";

  return (
    <label className={app.stats}>
      <input
        type="checkbox"
        required={required}
        disabled={disabled}
        checked={checked}
        style={{ accentColor: theme.palette.primary.main }}
        onChange={() => onclick((prev) => ({ ...prev, [label]: !prev[label] }))}
      ></input>
      <Typography>{t(labelKey)}</Typography>
    </label>
  );
};

export default Checkbox;

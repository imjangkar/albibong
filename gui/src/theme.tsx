import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      main: "#64d3ff",
    },
    background: {
      paper: "#0f3c4e",
      default: "#0b2a37",
    },
  },
  typography: {
    fontFamily: "monospace",
    h1: {
      fontSize: "2rem",
      fontWeight: "bold",
    },
    h2: {
      fontSize: "1.5rem",
      fontWeight: "bold",
    },
    h3: {
      fontSize: "1.25rem",
      fontWeight: "bold",
    },
    h4: {
      fontSize: "1rem",
      fontWeight: "bold",
    },
    h5: {
      fontSize: "0.75rem",
    },
    body1: {
      fontSize: "1rem",
    },
    body2: {
      fontSize: "0.8rem",
    },
  },
  components: {
    MuiInput: {
      styleOverrides: {
        root: {
          fontSize: "1.5rem",
          fontWeight: "bold",
          minWidth: "80px",
          "&::before": {
            borderBottom: "0px",
          },
          "&::after": {
            borderBottom: "0px",
          },
        },
      },
    },
  },
});

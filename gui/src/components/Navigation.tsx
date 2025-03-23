import {
  CSSObject,
  Divider,
  IconButton,
  ListItemIcon,
  Theme,
  Toolbar,
  Typography,
  styled,
} from "@mui/material";
import MuiAppBar, { AppBarProps as MuiAppBarProps } from "@mui/material/AppBar";
import MuiDrawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";

import {
  Agriculture,
  Assessment,
  ChevronLeft,
  ChevronRight,
  Speed,
  Map,
} from "@mui/icons-material";
import classNames from "classnames";
import { WorldContext } from "../providers/WorldProvider";

import styles from "./Navigation.module.css";

const drawerWidth = 240;

const openedMixin = (theme: Theme): CSSObject => ({
  width: drawerWidth,
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: "hidden",
});

const closedMixin = (theme: Theme): CSSObject => ({
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: "hidden",
  width: `calc(${theme.spacing(8)} + 1px)`,
  // [theme.breakpoints.up("sm")]: {
  //   width: `calc(${theme.spacing(8)} + 1px)`,
  // },
});

const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "flex-end",
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}));

interface AppBarProps extends MuiAppBarProps {
  open?: boolean;
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})<AppBarProps>(({ theme, open }) => ({
  paddingLeft: theme.spacing(7),
  zIndex: theme.zIndex.drawer - 1,
  transition: theme.transitions.create(["width", "margin"], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    paddingLeft: 0,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const Drawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => {
  return {
    width: drawerWidth,
    flexShrink: 0,
    whiteSpace: "nowrap",
    boxSizing: "border-box",
    ...(open && {
      ...openedMixin(theme),
      "& .MuiDrawer-paper": openedMixin(theme),
    }),
    ...(!open && {
      ...closedMixin(theme),
      "& .MuiDrawer-paper": closedMixin(theme),
    }),
  };
});

const Navigation = () => {
  const links = [
    { pageName: "DPS Meter", url: "/", icon: <Speed /> },
    {
      pageName: "Dungeon Tracker",
      url: "/dungeon-tracker",
      icon: <Assessment />,
    },
    {
      pageName: "Farming Tracker",
      url: "/farming-tracker",
      icon: <Agriculture />,
    },
    {
      pageName: "Map Radar",
      url: "/dps-marker",
      icon: <Map />,
    }
  ];
  const navigate = useNavigate();

  const [open, setOpen] = React.useState(false);
  const { me, world, healthCheck } = useContext(WorldContext);

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  const healthCheckIndicator = classNames({
    [styles.healthCheckDiv]: true,
    [styles.passed]: healthCheck.status == "passed",
    [styles.failed]: healthCheck.status == "failed",
  });

  return (
    <>
      <AppBar position="fixed" open={open} color="secondary">
        <Toolbar className={styles.toolbar}>
          <div className={styles.data}>
            <Typography>
              USERNAME: <b>{me.username}</b>
            </Typography>
            <Typography>
              CURRENT MAP: <b>{world.map}</b>
            </Typography>
            <Typography>
              CURRENT DUNGEON: <b>{world.dungeon}</b>
            </Typography>
          </div>
          <div className={styles.data}>
            <div className={healthCheckIndicator} />
            {healthCheck.status == "failed" && <p>{healthCheck.message}</p>}
          </div>
        </Toolbar>
      </AppBar>
      <Drawer variant="permanent" open={open}>
        <DrawerHeader>
          {open ? (
            <IconButton onClick={handleDrawerClose}>
              <ChevronLeft />
            </IconButton>
          ) : (
            <IconButton onClick={handleDrawerOpen}>
              <ChevronRight />
            </IconButton>
          )}
        </DrawerHeader>
        <Divider />
        <List>
          {links.map((link, index) => {
            return (
              <ListItem key={index} disablePadding sx={{ display: "block" }}>
                <ListItemButton
                  sx={{
                    minHeight: 48,
                    justifyContent: open ? "initial" : "center",
                    px: 2.5,
                  }}
                  onClick={() => {
                    navigate(link.url);
                    handleDrawerClose();
                  }}
                >
                  <ListItemIcon
                    sx={{
                      minWidth: 0,
                      mr: open ? 3 : "auto",
                      justifyContent: "center",
                    }}
                  >
                    {link.icon}
                  </ListItemIcon>
                  <ListItemText
                    primary={link.pageName}
                    sx={{ opacity: open ? 1 : 0 }}
                  />
                </ListItemButton>
              </ListItem>
            );
          })}
        </List>
      </Drawer>
    </>
  );
};

export default Navigation;

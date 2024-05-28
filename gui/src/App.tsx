import { useContext, useEffect } from "react";
import { Outlet, RouterProvider, createBrowserRouter } from "react-router-dom";
import Navigation from "./components/Navigation";
import DPSMeter from "./pages/DPSMeter";
import WorldProvider, { WorldContext } from "./providers/WorldProvider";
import WebsocketProvider, {
  WebsocketContext,
} from "./providers/WebsocketProvider";
import DungeonTracker from "./pages/DungeonTracker";
import { theme } from "./theme";

const App = () => {
  return (
    <WebsocketProvider>
      <WorldProvider>
        <Init>
          <Router />
        </Init>
      </WorldProvider>
    </WebsocketProvider>
  );
};

const container = {
  width: "100%",
  padding: "96px 64px 64px 128px",
  backgroundColor: theme.palette.background.default,
  minHeight: "100vh",
};

const Layout = () => {
  return (
    <>
      <Navigation />
      <div style={container}>
        <Outlet />
      </div>
    </>
  );
};

const Router = () => {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Layout />,
      children: [
        {
          path: "/",
          element: <DPSMeter />,
        },
        {
          path: "/dungeon-tracker",
          element: <DungeonTracker />,
        },
      ],
    },
  ]);
  return <RouterProvider router={router} />;
};

const Init = ({ children }: { children: React.ReactNode }) => {
  const { lastMessage, sendMessage } = useContext(WebsocketContext);
  const {
    initPlayer,
    initWorld,
    updateFame,
    updateReSpec,
    updateSilver,
    updateLocation,
    updateIsDPSMeterRunning,
    updateParty,
    updateDungeon,
  } = useContext(WorldContext);

  useEffect(() => {
    if (lastMessage !== null) {
      let ws_event = JSON.parse(lastMessage.data);
      if (ws_event.type == "init_world") {
        initWorld(ws_event.payload.me, ws_event.payload.world);
      } else if (ws_event.type == "init_character") {
        initPlayer(ws_event.payload);
      } else if (ws_event.type == "update_fame") {
        updateFame(ws_event.payload.fame_gained);
      } else if (ws_event.type == "update_re_spec") {
        updateReSpec(ws_event.payload.re_spec_gained);
      } else if (ws_event.type == "update_silver") {
        updateSilver(ws_event.payload.username, ws_event.payload.silver_gained);
      } else if (ws_event.type == "update_location") {
        updateLocation(ws_event.payload.map, ws_event.payload.dungeon);
      } else if (ws_event.type == "update_dps") {
        updateParty(ws_event.payload.party_members);
      } else if (ws_event.type == "update_is_dps_meter_running") {
        updateIsDPSMeterRunning(ws_event.payload.value);
      } else if (ws_event.type == "update_dungeon") {
        updateDungeon(ws_event.payload.list_dungeon);
      }
    }
  }, [lastMessage]);

  useEffect(() => {
    sendMessage({
      type: "refresh_dungeon_list",
      payload: { value: true },
    });
  }, []);

  return <>{children}</>;
};

export default App;

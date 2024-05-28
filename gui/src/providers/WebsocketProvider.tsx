import React from "react";
import useWebSocket, {
  Options,
  ReadyState,
  SendMessage,
} from "react-use-websocket";

type EventData = {
  type: string;
  payload: {};
};
type WebsocketContextData = {
  sendToBE: SendMessage;
  sendMessage: (ev: EventData) => void;
  lastMessage: MessageEvent<any> | null;
  connectionStatus: string;
};

export const WebsocketContext = React.createContext<WebsocketContextData>({
  sendToBE: () => {},
  sendMessage: () => {},
  lastMessage: null,
  connectionStatus: "",
});

type WebsocketProviderProps = {
  children: React.ReactNode;
};

const OPTIONS: Options = {
  retryOnError: true,
  shouldReconnect: (_) => true,
  reconnectAttempts: Infinity,
  reconnectInterval: 1000,
};

const WebsocketProvider = ({ children }: WebsocketProviderProps) => {
  const socketUrl = "ws://localhost:8081";

  const {
    sendMessage: sendToBE,
    lastMessage,
    readyState,
  } = useWebSocket(socketUrl, OPTIONS);

  const sendMessage = (ev: EventData) => {
    sendToBE(JSON.stringify(ev));
  };

  const connectionStatus = {
    [ReadyState.CONNECTING]: "Connecting",
    [ReadyState.OPEN]: "Open",
    [ReadyState.CLOSING]: "Closing",
    [ReadyState.CLOSED]: "Closed",
    [ReadyState.UNINSTANTIATED]: "Uninstantiated",
  }[readyState];

  return (
    <WebsocketContext.Provider
      value={{
        sendToBE,
        sendMessage,
        lastMessage,
        connectionStatus,
      }}
    >
      {children}
    </WebsocketContext.Provider>
  );
};

export default WebsocketProvider;

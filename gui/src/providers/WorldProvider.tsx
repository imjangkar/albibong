import React, { useState } from "react";

type PlayerCharacter = {
  username: string;
  fame: number;
  re_spec: number;
  silver: number;
  weapon: string;
};

type PartyMember = {
  username: string;
  damage_percent: number;
  damage_dealt: number;
  heal_percent: number;
  healing_dealt: number;
  combat_duration: string;
  dps: number;
  weapon: string;
};

export type Dungeon = {
  id: string;
  type: string;
  name: string;
  tier: number;
  fame: number;
  silver: number;
  re_spec: number;
  date_time: string;
  time_elapsed: string;
};

export type World = {
  map: string;
  dungeon: string;
  isDPSMeterRunning: boolean;
  party: PartyMember[];
  list_dungeon: Dungeon[];
};

type WorldContextData = {
  me: PlayerCharacter;
  world: World;
  dungeonFilter: string[];
  setWorld: any;
  initWorld: (me: PlayerCharacter, world: World) => void;
  initPlayer: (me: PlayerCharacter) => void;
  updateFame: (fame_gained: number) => void;
  updateReSpec: (re_spec_gained: number) => void;
  updateSilver: (username: string, silver_gained: number) => void;
  updateLocation: (map: string, dungeon: string) => void;
  updateIsDPSMeterRunning: (value: boolean) => void;
  updateParty: (party: PartyMember[]) => void;
  updateDungeon: (list_dungeon: Dungeon[]) => void;
};

export const WorldContext = React.createContext<WorldContextData>({
  me: {
    username: "Not initialized",
    fame: 0,
    re_spec: 0,
    silver: 0,
    weapon: "Not initialized",
  },
  world: {
    map: "None",
    dungeon: "None",
    isDPSMeterRunning: false,
    party: [],
    list_dungeon: [],
  },
  dungeonFilter: [],
  setWorld: () => {},
  initWorld: () => {},
  initPlayer: () => {},
  updateFame: () => {},
  updateReSpec: () => {},
  updateSilver: () => {},
  updateLocation: () => {},
  updateIsDPSMeterRunning: () => {},
  updateParty: () => {},
  updateDungeon: () => {},
});

type WorldProviderProps = {
  children: React.ReactNode;
};

const WorldProvider = ({ children }: WorldProviderProps) => {
  const [me, setMe] = useState<PlayerCharacter>({
    username: "Not initialized",
    fame: 0,
    re_spec: 0,
    silver: 0,
    weapon: "Not initialized",
  });

  const [world, setWorld] = useState<World>({
    map: "None",
    dungeon: "None",
    isDPSMeterRunning: false,
    party: [],
    list_dungeon: [],
  });

  const [dungeonFilter, setDungeonFilter] = useState<string[]>(["ALL"]);

  const initWorld = (me: PlayerCharacter, world: World) => {
    setMe({
      username: me.username,
      fame: me.fame,
      re_spec: me.re_spec,
      silver: me.silver,
      weapon: me.weapon,
    });
    setWorld({
      map: world.map,
      dungeon: world.dungeon,
      isDPSMeterRunning: world.isDPSMeterRunning,
      party: [],
      list_dungeon: [],
    });
  };

  const initPlayer = (me: PlayerCharacter) => {
    setMe({
      username: me.username,
      fame: me.fame,
      re_spec: me.re_spec,
      silver: me.silver,
      weapon: me.weapon,
    });
  };

  const updateFame = (fame_gained: number) => {
    setMe((prev) => ({
      ...prev,
      fame: fame_gained,
    }));
  };

  const updateReSpec = (re_spec_gained: number) => {
    setMe((prev) => ({
      ...prev,
      re_spec: re_spec_gained,
    }));
  };

  const updateSilver = (username: string, silver_gained: number) => {
    if (username == me.username) {
      setMe((prev) => ({
        ...prev,
        silver: silver_gained,
      }));
    }
  };

  const updateLocation = (map: string, dungeon: string) =>
    setWorld((prev) => ({
      ...prev,
      map: map,
      dungeon: dungeon,
    }));

  const updateIsDPSMeterRunning = (value: boolean) => {
    setWorld((prev) => ({
      ...prev,
      isDPSMeterRunning: value,
    }));
  };

  const updateParty = (party: PartyMember[]) => {
    setWorld((prev) => ({
      ...prev,
      party: party,
    }));
  };

  const updateDungeon = (list_dungeon: Dungeon[]) => {
    setWorld((prev) => ({
      ...prev,
      list_dungeon: list_dungeon,
    }));
    updateDungeonFilter(list_dungeon);
  };

  const updateDungeonFilter = (list_dungeon: Dungeon[]) => {
    let dungeonFilter = new Set<string>();
    dungeonFilter.add("ALL");
    list_dungeon.forEach((dungeon) => {
      dungeonFilter.add(dungeon.type);
    });
    setDungeonFilter([...dungeonFilter]);
  };

  return (
    <WorldContext.Provider
      value={{
        me,
        world,
        dungeonFilter,
        setWorld,
        initWorld,
        initPlayer,
        updateFame,
        updateReSpec,
        updateSilver,
        updateLocation,
        updateIsDPSMeterRunning,
        updateParty,
        updateDungeon,
      }}
    >
      {children}
    </WorldContext.Provider>
  );
};

export default WorldProvider;

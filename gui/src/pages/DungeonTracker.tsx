import app from "../App.module.css";
import {
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  Typography,
} from "@mui/material";
import { useContext, useEffect, useState } from "react";
import { Dungeon, WorldContext } from "../providers/WorldProvider";
import DungeonCard from "../components/DungeonCard";

const DungeonTracker = () => {
  const { world, dungeonFilter } = useContext(WorldContext);

  const [filteredDungeon, setFilteredDungeon] = useState<Dungeon[]>([]);

  const [selectedFilter, setSelectedFilter] = useState("ALL");

  const handleFilterDungeon = (selectedFilter: string) => {
    if (selectedFilter == "ALL") {
      setFilteredDungeon(world.list_dungeon);
    } else {
      let filteredData = world.list_dungeon.filter(
        (dungeon) => dungeon.type == selectedFilter
      );
      setFilteredDungeon(filteredData);
    }
  };

  useEffect(() => {
    handleFilterDungeon(selectedFilter);
  }, [world.list_dungeon]);

  useEffect(() => {
    handleFilterDungeon(selectedFilter);
  }, [selectedFilter]);

  return (
    <div className={app.container}>
      <Typography variant="h1">Dungeon Tracker</Typography>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">
          Filter by Dungeon Type
        </InputLabel>
        <Select
          value={selectedFilter}
          label="Filter by Dungeon Type"
          onChange={(e) => setSelectedFilter(e.target.value)}
        >
          {dungeonFilter.map((filter, index) => (
            <MenuItem key={index} value={filter}>
              {filter}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      {filteredDungeon.length > 0 ? (
        filteredDungeon.map((dungeon) => {
          return <DungeonCard key={dungeon.id} dungeon={dungeon}></DungeonCard>;
        })
      ) : (
        <p>No dungeon</p>
      )}
    </div>
  );
};

export default DungeonTracker;

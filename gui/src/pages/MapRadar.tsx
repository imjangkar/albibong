import { useContext, useEffect, useRef, useState } from "react";
import { Box, Button, Container, Paper, Typography, Modal } from "@mui/material";
import app from "../App.module.css";
import { WorldContext } from "../providers/WorldProvider";
import RadarRendering from "../utils/rendering";

const MapRadar = () => {
    const canvasRef = useRef<HTMLCanvasElement>(null);

    const { radarWidget, radarPosition } = useContext(WorldContext);
    // const { radarPosition } = useContext(WorldContext);
    const [zoom, setZoom] = useState(3.5);

    const [displayedSettings, setDisplayedSettings] = useState({
        object_types: ['RESOURCE', 'DUNGEONS', 'MOBS'],
        dungeons: ['SOLO', 'AVALON', 'GROUP', 'CORRUPTED', 'HELLGATE', 'ROAMING', 'DISPLAY_NAME'],
        resources: ['FIBER', 'WOOD', 'ROCK', 'HIDE', 'ORE'],
        tiers: [3, 4, 5, 6, 7, 8],
        enchants: [0, 1, 2, 3]
    });
    
    const [activeTab, setActiveTab] = useState('map');

    // const radarPosition = {
    //     x: 180,
    //     y: 100
    // };

    // const radarWidget = {
    //     harvestable_list:[{
    //         "id": 178765,
    //         "type": 16,
    //         "tier": 4,
    //         "location": {
    //             "x": 0,
    //             "y": 0
    //             // "x": 185.5,
    //             // "y": 115.0
    //         },
    //         "enchant": 3,
    //         "size": 1,
    //         "unique_name": "hide_4_3",
    //         "item_type": "HIDE",
    //         "debug": {}
    //     }],
    //     dungeon_list: [
    //         {
    //             "id": 178765,
    //             "tier": 4,
    //             "location": {
    //                 "x": 185.5,
    //                 "y": 115.0
    //             },
    //             "enchant": 3,
    //             "dungeon_type": "GROUP",
    //             "name": "Dungeon",
    //             "unique_name": "group_dungeon",
    //             "is_consumable": false,
    //             "debug": {}
    //         },
    //         {
    //             "id": 178765,
    //             "tier": 4,
    //             "location": {
    //                 "x": 180.0,
    //                 "y": 89.1
    //             },
    //             "enchant": 1,
    //             "dungeon_type": "SOLO",
    //             "name": "T4_PORTAL_ROYAL_CONSUMABLE_SOLO ",
    //             "unique_name": "solo_dungeon",
    //             "is_consumable": true,
    //             "debug": {}
    //         }
    //     ],
    //     chest_list: [
    //         {
    //             "id": 20,
    //             "location": {
    //                 "x": 150.5,
    //                 "y": 115.0
    //             },
    //             "name1": "T4",
    //             "name2": "CHEST",
    //             "chest_name": "T4_CHEST",
    //             "enchant": 3,
    //             "debug": {}
    //         },
    //     ],
    //     mist_list: [{
    //         "id": 178765,
    //         "location": {
    //             "x": 185.5,
    //             "y": 100.0
    //         },
    //         "name": "T4_MIST",
    //         "enchant": 4,
    //         "debug": {}
    //     }],
    //     mob_list: [],
    //     players_list: [{
    //         "id": 178765,
    //         "faction": 0,
    //         "username": "Username",
    //         "guild": "Guild",
    //         "alliance": "Alliance",
    //         "equipments": ["None", "None", "None", "None", "None", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //         // "equipments": ["T6_MAIN_DAGGER", "T6_OFF_TORCH", "T6_HEAD_LEATHER_SET3", "T6_ARMOR_LEATHER_SET2", "T6_SHOES_LEATHER_SE", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //     },
    //     {
    //         "id": 178765,
    //         "faction": 255,
    //         "username": "Username",
    //         "guild": "Guild",
    //         "alliance": "Alliance",
    //         "equipments": ["None", "None", "None", "None", "None", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //         // "equipments": ["T6_MAIN_DAGGER", "T6_OFF_TORCH", "T6_HEAD_LEATHER_SET3", "T6_ARMOR_LEATHER_SET2", "T6_SHOES_LEATHER_SE", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //     },
    //     {
    //         "id": 178765,
    //         "faction": 0,
    //         "username": "Username",
    //         "guild": "Guild",
    //         "alliance": "Alliance",
    //         "equipments": ["None", "None", "None", "None", "None", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //         // "equipments": ["T6_MAIN_DAGGER", "T6_OFF_TORCH", "T6_HEAD_LEATHER_SET3", "T6_ARMOR_LEATHER_SET2", "T6_SHOES_LEATHER_SE", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //     },
    //     {
    //         "id": 178765,
    //         "faction": 0,
    //         "username": "Username",
    //         "guild": "Guild",
    //         "alliance": "Alliance",
    //         "equipments": ["None", "None", "None", "None", "None", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //         // "equipments": ["T6_MAIN_DAGGER", "T6_OFF_TORCH", "T6_HEAD_LEATHER_SET3", "T6_ARMOR_LEATHER_SET2", "T6_SHOES_LEATHER_SE", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //     },
    //     {
    //         "id": 178765,
    //         "faction": 0,
    //         "username": "Username",
    //         "guild": "Guild",
    //         "alliance": "Alliance",
    //         "equipments": ["None", "None", "None", "None", "None", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //         // "equipments": ["T6_MAIN_DAGGER", "T6_OFF_TORCH", "T6_HEAD_LEATHER_SET3", "T6_ARMOR_LEATHER_SET2", "T6_SHOES_LEATHER_SE", "T8_BAG", "T4_CAPEITEM_FW_MARTLOCK@3", "T8_MOUNT_DIREBOAR_FW_LYMHURST_ELITE", "None", "None"],
    //     }],
    // };


    useEffect(() => {
        const canvas = canvasRef.current;
        const ctx = canvas?.getContext('2d');
        if (canvas && ctx) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.save();
            radarWidget.harvestable_list.forEach(resource => {
                RadarRendering.renderResource(ctx, canvas, radarPosition, resource, zoom, displayedSettings);
            });

            radarWidget.dungeon_list.forEach(dungeon => {
                RadarRendering.renderDungeon(ctx, canvas, radarPosition, dungeon, zoom, displayedSettings);
            });

            radarWidget.chest_list.forEach(chest => {
                RadarRendering.renderChest(ctx, canvas, radarPosition, chest, zoom, displayedSettings);
            });

            radarWidget.mist_list.forEach(mist => {
                RadarRendering.renderMist(ctx, canvas, radarPosition, mist, zoom, displayedSettings);
            });

            radarWidget.mob_list.forEach(mob => {
                RadarRendering.renderMob(ctx, canvas, radarPosition, mob, zoom, displayedSettings);
            });

            ctx.fillStyle = 'yellow';
            ctx.beginPath();
            ctx.fill();
            ctx.restore();

            RadarRendering.renderCenter(ctx, canvas);
            RadarRendering.renderTheScreenView(ctx, canvas, zoom);
        }

    }, [radarPosition, zoom, radarWidget, displayedSettings]);

    return (
        // <div className={app.container}>
        <Container className={app.container} sx={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', textAlign: 'left' }}>
            <Box sx={{ alignSelf: 'flex-end', marginBottom: '10px' }}>
                <Button variant="contained" onClick={() => setActiveTab('settings')}>Settings</Button>
                {activeTab === 'settings' && (
                    <Modal
                        open={true}
                        onClose={() => setActiveTab('')}
                        aria-labelledby="settings-modal-title"
                        aria-describedby="settings-modal-description"
                    >
                        <Paper sx={{ padding: '10px', maxHeight: '500px', overflowY: 'scroll', margin: 'auto', marginTop: '10%', width: '50%' }}>
                            <Typography id="settings-modal-title" variant="h6">Settings</Typography>
                            <Box sx={{ marginBottom: '10px' }}>
                                <Typography variant="subtitle1">Display Settings</Typography>
                                <Box sx={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                                    <Box>
                                        <Typography variant="body1">Object Types</Typography>
                                        {['RESOURCE', 'DUNGEONS', 'MOBS'].map(type => (
                                            <Button
                                                key={type}
                                                variant={displayedSettings.object_types.includes(type) ? "contained" : "outlined"}
                                                sx={{ margin: '5px' }}
                                                onClick={() => setDisplayedSettings(prev => ({
                                                    ...prev,
                                                    object_types: prev.object_types.includes(type)
                                                        ? prev.object_types.filter(t => t !== type)
                                                        : [...prev.object_types, type]
                                                }))}
                                            >
                                                {type}
                                            </Button>
                                        ))}
                                        <Typography variant="body1">Resources</Typography>
                                        {['FIBER', 'WOOD', 'ROCK', 'HIDE', 'ORE'].map(resource => (
                                            <Button
                                                key={resource}
                                                variant={displayedSettings.resources.includes(resource) ? "contained" : "outlined"}
                                                sx={{ margin: '5px' }}
                                                onClick={() => setDisplayedSettings(prev => ({
                                                    ...prev,
                                                    resources: prev.resources.includes(resource)
                                                        ? prev.resources.filter(r => r !== resource)
                                                        : [...prev.resources, resource]
                                                }))}
                                            >
                                                {resource}
                                            </Button>
                                        ))}
                                    </Box>
                                    <Box>
                                        <Typography variant="body1">Dungeons</Typography>
                                        {['SOLO', 'AVALON', 'GROUP', 'CORRUPTED', 'HELLGATE', 'ROAMING', 'DISPLAY_NAME'].map(dungeon => (
                                            <Button
                                                key={dungeon}
                                                variant={displayedSettings.dungeons.includes(dungeon) ? "contained" : "outlined"}
                                                sx={{ margin: '5px' }}
                                                onClick={() => setDisplayedSettings(prev => ({
                                                    ...prev,
                                                    dungeons: prev.dungeons.includes(dungeon)
                                                        ? prev.dungeons.filter(d => d !== dungeon)
                                                        : [...prev.dungeons, dungeon]
                                                }))}
                                            >
                                                {dungeon}
                                            </Button>
                                        ))}
                                    </Box>
                                    <Box>
                                        <Typography variant="body1">Tiers</Typography>
                                        {[3, 4, 5, 6, 7, 8].map(tier => (
                                            <Button
                                                key={tier}
                                                variant={displayedSettings.tiers.includes(tier) ? "contained" : "outlined"}
                                                sx={{ margin: '5px' }}
                                                onClick={() => setDisplayedSettings(prev => ({
                                                    ...prev,
                                                    tiers: prev.tiers.includes(tier)
                                                        ? prev.tiers.filter(t => t !== tier)
                                                        : [...prev.tiers, tier]
                                                }))}
                                            >
                                                Tier {tier}
                                            </Button>
                                        ))}
                                    </Box>
                                    <Box>
                                        <Typography variant="body1">Enchant Levels</Typography>
                                        {[0, 1, 2, 3].map(level => (
                                            <Button
                                                key={level}
                                                variant={displayedSettings.enchants.includes(level) ? "contained" : "outlined"}
                                                sx={{ margin: '5px' }}
                                                onClick={() => setDisplayedSettings(prev => ({
                                                    ...prev,
                                                    enchants: prev.enchants.includes(level)
                                                        ? prev.enchants.filter(e => e !== level)
                                                        : [...prev.enchants, level]
                                                }))}
                                            >
                                                Enchant {level}
                                            </Button>
                                        ))}
                                    </Box>
                                </Box>
                            </Box>
                            <Button variant="contained" onClick={() => setActiveTab('')}>Close</Button>
                        </Paper>
                    </Modal>
                )}
            </Box>
            <Box sx={{ textAlign: 'left' }}>
                <Paper sx={{ padding: '5px', border: '1px solid black' }}>
                    <Typography>Zoom: {zoom.toFixed(1)}</Typography>
                </Paper>
                <Paper sx={{ padding: '5px', border: '1px solid black' }}>
                    <Typography>Position: x {radarPosition.x.toFixed(1)} y {radarPosition.y.toFixed(1)}</Typography>
                </Paper>
            </Box>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', width: '100%' }}>
                <Box sx={{ flex: 1, width: 500, height: 508, margin: '0px 0px', textAlign: 'center', border: '2px solid blue', overflow: 'hidden', position: 'relative' }}>
                    <canvas ref={canvasRef} width={500} height={500} style={{ border: '2px solid red', position: 'absolute', transform: `translate(-50%, 0%)` }} />
                </Box>
                <Box sx={{ flex: 1, textAlign: 'left', marginTop: '20px', marginLeft: '20px' }}>
                    <Box sx={{ maxHeight: '500px', overflowY: 'auto' }}>
                        {radarWidget.players_list.length > 0 && radarWidget.players_list
                            .sort((a, b) => Number(b.faction) - Number(a.faction))
                            .map((player) => (
                                <Paper key={player.id} sx={{ padding: '10px', marginBottom: '10px', border: '1px solid black' }}>
                                    <Box sx={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                                        <img
                                            src={`/public/mapMarker/faction/faction_${player.faction}.png`}
                                            alt={`Faction ${player.faction}`}
                                            style={{ width: '34px', height: '34px' }}
                                        />
                                        <Typography variant="body1">{player.username}, ID: {player.id}</Typography>
                                    </Box>
                                    <Typography variant="body1">Guild: {player.guild}, Alliance: {player.alliance}</Typography>
                                    <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: '10px' }}>
                                        {player.equipments.map((equipment, index) => (
                                            equipment === "None" ? (
                                                <Box
                                                    key={index}
                                                    sx={{ width: '40px', height: '40px', backgroundColor: '#333', border: '2px solid orange' }}
                                                />
                                            ) : (
                                                <img
                                                    key={index}
                                                    src={`https://render.albiononline.com/v1/item/${equipment}`}
                                                    alt={equipment}
                                                    style={{ width: '40px', height: '40px', border: '2px solid orange' }}
                                                />
                                            )
                                        ))}
                                    </Box>
                                </Paper>
                            ))}
                    </Box>
                </Box>
            </Box>
            <Box sx={{ textAlign: 'center' }}>
                <Button variant="contained" onClick={() => setZoom(zoom => Math.min(zoom + 0.2, 5))}>Zoom In</Button>
                <Button variant="contained" onClick={() => setZoom(zoom => Math.max(zoom - 0.2, 1))}>Zoom Out</Button>
            </Box>
        </Container>
        // </div>
    );
};

export default MapRadar;
class RadarRendering {
    static rotation = 45;
    static ResourceSize = 45;
    static mistSize = 35;
    static ScreenRenderSize = 28;

    static getDistance(radarPostion: any, itemPostion: any){
        const rX = itemPostion.x - radarPostion.x; // 0 - 0 = 0
        const rY = itemPostion.y - radarPostion.y; // 20 - 0 = 20

        return Math.sqrt(rX * rX + rY * rY); // Math.sqrt(0 + 400) = 20
    }

    static getRelativePositionX(radarPostion: any, itemPostion: any, zoom: number) {
        const angle = (Math.PI / 180) * this.rotation;
        const relativeX = itemPostion.x - radarPostion.x;
        const relativeY = itemPostion.y - radarPostion.y;
        return (-1 * relativeX * Math.cos(angle) - relativeY * Math.sin(angle)) * zoom;
    }

    static getRelativePositionY(radarPostion: any, itemPostion: any, zoom: number) {
        const angle = (Math.PI / 180) * this.rotation;
        const relativeY = itemPostion.y - radarPostion.y;
        return (relativeY * Math.cos(angle) + relativeY * Math.sin(angle)) * zoom;
    }

    static renderDistance(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, radarPosition: any, location: any, itemSize: number, rX: number, rY: number) {
        ctx.font = "12px Arial";
        ctx.fillStyle = 'red';

        const distance = this.getDistance(radarPosition, location)
        
        const adjustedX = canvas.width / 2 - rX - itemSize / 2 + 5;
        const adjustedY = canvas.height / 2 - rY - itemSize / 2 + itemSize + 10;
        
        ctx.fillText(distance.toString(), adjustedX, adjustedY);;
    }

    static renderValue(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, itemSize: number, rX: number, rY: number, value: string) {
        ctx.font = "12px Arial";
        ctx.fillStyle = 'white';

        const textWidth = ctx.measureText(value).width;
        const adjustedX = canvas.width / 2 - rX - textWidth / 2;
        const adjustedY = canvas.height / 2 - rY - itemSize / 2 - 5;
        
        ctx.fillText(value, adjustedX, adjustedY);
    }

    static renderButterfly(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, itemSize: number, rX: number, rY: number, enchant: number) {
        if (enchant === 0) {
            return;
        }

        const butterfly_map: { [key: number]: string } = {
            1: 'butterfly_uncommon',
            2: 'butterfly_rare',
            3: 'butterfly_epic',
            4: 'butterfly_legendary',
        }

         /* Render Iteam */
         const img = new Image();
         img.src = `/public/mapMarker/butterfly/${butterfly_map[enchant]}.png`;

        const adjustedX = canvas.width / 2 - rX - itemSize / 2 + 15;
        const adjustedY = canvas.height / 2 - rY - itemSize / 2 - 10;

        
        img.onload = () => {
            ctx.drawImage(img, adjustedX, adjustedY, 45, 45);
        }
    }

    static renderEnemyObject(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, itemSize: number, rX: number, rY: number) {

         /* Render Iteam */
         const img = new Image();
         img.src = `/public/mapMarker/additionals/auto_attack.png`;

        const adjustedX = canvas.width / 2 - rX - itemSize / 2 - 15;
        const adjustedY = canvas.height / 2 - rY - itemSize / 2 - 10;

        
        img.onload = () => {
            ctx.drawImage(img, adjustedX, adjustedY, 35, 35);
        }
    }

    static renderUnknowResource(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, radarPosition: any, resource: any, zoom: number) {
        const rX =  this.getRelativePositionX(radarPosition, resource.location, zoom);
        const rY =  this.getRelativePositionY(radarPosition, resource.location, zoom);

        this.renderDistance(ctx, canvas, radarPosition, resource.location, this.ResourceSize, rX, rY);
        this.renderValue(ctx, canvas, this.ResourceSize, rX, rY, `${resource.id} || ${resource.type}`);  
    }

    static renderTheScreenView(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, zoom: number) {
        ctx.strokeStyle = 'blue';
        ctx.beginPath();
        //TODO not fully works
        ctx.arc(canvas.width / 2, canvas.height / 2, this.ScreenRenderSize * zoom, 0, 2 * Math.PI);
        ctx.stroke();
    }

    static renderCenter(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement) {
        ctx.fillStyle = 'green';
        ctx.beginPath();
        ctx.arc(canvas.width / 2, canvas.height / 2, 5, 0, 2 * Math.PI);
        ctx.fill();
    }

    static renderResource(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, radarPosition: any, resource: any, zoom: number, displayedSettings: any) {
        if (!displayedSettings.object_types.includes('RESOURCE')) {
            return;
        }
        
        if (!resource.size && resource.item_type !== "unknown") {
            return;
        }

        if (resource.item_type === "unknown") {
            this.renderUnknowResource(ctx, canvas, radarPosition, resource, zoom);
            return;
        }

        const rX =  this.getRelativePositionX(radarPosition, resource.location, zoom);
        const rY =  this.getRelativePositionY(radarPosition, resource.location, zoom);
        
        /* Check if resource is displayed */
        if (!displayedSettings.resources.includes(resource.item_type)) {
            return;
        }
        if (!displayedSettings.tiers.includes(resource.tier)) {
            return;
        }
        if (!displayedSettings.enchants.includes(resource.enchant)) {
            return;
        }


        /* Render Iteam */
        const img = new Image();
        img.src = `/public/mapMarker/resources/${resource.unique_name}.png`;
        img.onload = () => {
            ctx.drawImage(img, canvas.width / 2 - rX - this.ResourceSize / 2, canvas.height / 2 - rY - this.ResourceSize / 2, this.ResourceSize, this.ResourceSize);
        };

        /* Render Distance */        
        // this.renderDistance(ctx, canvas, radarPosition, resource.location, this.ResourceSize, rX, rY);

        /* Render stock value */
        this.renderValue(ctx, canvas, this.ResourceSize, rX, rY, resource.size);
    }

    static renderDungeon(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, radarPosition: any, dungeon: any, zoom: number, displayedSettings: any) {
        const rX =  this.getRelativePositionX(radarPosition, dungeon.location, zoom);
        const rY =  this.getRelativePositionY(radarPosition, dungeon.location, zoom);

        
        if(!displayedSettings.object_types.includes('DUNGEONS') && !dungeon.is_consumable) {
            return;
        }

        if(!displayedSettings.dungeons.includes('ROAMING') && dungeon.is_consumable) {
            return;
        }

        if(!displayedSettings.dungeons.includes(dungeon.dungeon_type)) {
            return;
        }
        
        
        
        /* Render Iteam */
        const img = new Image();
        img.src = `/public/mapMarker/dungeons/${dungeon.unique_name}.png`;
        
        img.onload = () => {
            ctx.drawImage(img, canvas.width / 2 - rX - this.ResourceSize / 2, canvas.height / 2 - rY - this.ResourceSize / 2, this.ResourceSize, this.ResourceSize);
        };


        this.renderButterfly(ctx, canvas, this.ResourceSize, rX, rY, dungeon.enchant);

        /* Render Distance */        
        // this.renderDistance(ctx, canvas, radarPosition, resource.location, this.ResourceSize, rX, rY);

        if(dungeon.is_consumable) {
            this.renderEnemyObject(ctx, canvas, this.ResourceSize, rX, rY);
        }

        /* Render stock value */
        if(displayedSettings.dungeons.includes('DISPLAY_NAME')) {
            this.renderValue(ctx, canvas, this.ResourceSize, rX, rY, dungeon.name);
        }
    }

    static renderChest(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, radarPosition: any, chest: any, zoom: number, displayedSettings: any) {
        const rX =  this.getRelativePositionX(radarPosition, chest.location, zoom);
        const rY =  this.getRelativePositionY(radarPosition, chest.location, zoom);

        
        const chest_map: { [key: number]: string } = {
            0: 'chest_static',
            1: 'chest_green',
            2: 'chest_blue',
            3: 'chest_rare',
            4: 'chest_legendary',
        }
        
        
        
        /* Render Iteam */
        const img = new Image();
        img.src = `/public/mapMarker/chest/${chest_map[chest.enchant]}.png`;
        
        img.onload = () => {
            ctx.drawImage(img, canvas.width / 2 - rX - this.ResourceSize / 2, canvas.height / 2 - rY - this.ResourceSize / 2, this.ResourceSize, this.ResourceSize);
        };

        /* Render Distance */        
        // this.renderDistance(ctx, canvas, radarPosition, resource.location, this.ResourceSize, rX, rY);

        
        /* Render Chest Name if is static chest */
        if(chest.enchant === 0) {
            this.renderValue(ctx, canvas, this.ResourceSize, rX, rY, chest.name2);
        }
    }

    static renderMist(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, radarPosition: any, mist: any, zoom: number, displayedSettings: any) {
        const rX =  this.getRelativePositionX(radarPosition, mist.location, zoom);
        const rY =  this.getRelativePositionY(radarPosition, mist.location, zoom);

        /* Render Iteam */
        const img = new Image();
        img.src = `/public/mapMarker/mists/mist_${mist.enchant}.png`;
        
        img.onload = () => {
            ctx.drawImage(img, canvas.width / 2 - rX - this.mistSize / 2, canvas.height / 2 - rY - this.mistSize / 2, this.mistSize, this.mistSize);
        };

        /* Render Distance */        
        // this.renderDistance(ctx, canvas, radarPosition, resource.location, this.ResourceSize, rX, rY);
    }

    static renderMob(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, radarPosition: any, mob: any, zoom: number, displayedSettings: any) {
        if (!displayedSettings.object_types.includes('MOBS')) {
            return;
        }
        
        const rX =  this.getRelativePositionX(radarPosition, mob.location, zoom);
        const rY =  this.getRelativePositionY(radarPosition, mob.location, zoom);

        /* Render Iteam */
        // if(mob.mob_name !== "unknown12") {
        //     const img = new Image();
        //     img.src = `/public/mapMarker/mobs/${mob.mob_name}.png`;
            
        //     img.onload = () => {
        //         ctx.drawImage(img, canvas.width / 2 - rX - this.ResourceSize / 2, canvas.height / 2 - rY - this.ResourceSize / 2, this.ResourceSize, this.ResourceSize);
        //     };
        // } else {
            ctx.fillStyle = 'purple';
            ctx.beginPath();
            ctx.arc(canvas.width / 2 - rX, canvas.height / 2 - rY, 10, 0, 2 * Math.PI);
            ctx.fill();
        // }


        /* Render Chest Name if is static chest */
        const mobName = `${mob.id} || ${mob.type_id}`;
        this.renderValue(ctx, canvas, this.ResourceSize, rX, rY, mobName);

    }



    
    
}

export default RadarRendering;
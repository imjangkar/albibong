import { red } from "@mui/material/colors";

class RadarRendering {
    static rotation = 45;
    static ResourceSize = 45;
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

        const adjustedX = canvas.width / 2 - rX - itemSize / 2 + 10;
        const adjustedY = canvas.height / 2 - rY - itemSize / 2 - 5;
        
        ctx.fillText(value, adjustedX, adjustedY);;
    }

    static renderCenter(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement) {
        ctx.fillStyle = 'green';
        ctx.beginPath();
        ctx.arc(canvas.width / 2, canvas.height / 2, 5, 0, 2 * Math.PI);
        ctx.fill();
    }

    static renderTheScreenView(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, zoom: number) {
        ctx.strokeStyle = 'blue';
        ctx.beginPath();
        //TODO not fully works
        ctx.arc(canvas.width / 2, canvas.height / 2, this.ScreenRenderSize * zoom, 0, 2 * Math.PI);
        ctx.stroke();
    }

    static renderUnknowResource(ctx: CanvasRenderingContext2D, canvas: HTMLCanvasElement, radarPosition: any, resource: any, zoom: number) {
        const rX =  this.getRelativePositionX(radarPosition, resource.location, zoom);
        const rY =  this.getRelativePositionY(radarPosition, resource.location, zoom);

        this.renderDistance(ctx, canvas, radarPosition, resource.location, this.ResourceSize, rX, rY);
        this.renderValue(ctx, canvas, this.ResourceSize, rX, rY, `${resource.id} || ${resource.type}`);  
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
        img.src = `https://render.albiononline.com/v1/item/${resource.unique_name}`;
        img.onload = () => {
            ctx.drawImage(img, canvas.width / 2 - rX - this.ResourceSize / 2, canvas.height / 2 - rY - this.ResourceSize / 2, this.ResourceSize, this.ResourceSize);
        };

        /* Render Distance */        
        // this.renderDistance(ctx, canvas, radarPosition, resource.location, this.ResourceSize, rX, rY);

        /* Render stock value */
        this.renderValue(ctx, canvas, this.ResourceSize, rX, rY, resource.size);
    }
}

export default RadarRendering;
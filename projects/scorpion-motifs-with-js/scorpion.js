// Derived class, specializes Block
class Scorpion extends Block {
    constructor(width, height, backColor, patchColor1, patchColor2) {
        super(width, height, backColor);
        this.patchColor1 = patchColor1;
        this.patchColor2 = patchColor2;
    }

    // Can you overload in JS?
    render(x, y) {
        this.ulx = x;
        this.uly = y;
        render();
    }

    render() {
        let patchWide = this.width / 2;
        let patchHigh = this.height / 2;
        let midX = this.ulx + patchWide;
        let midY = this.uly + patchHigh;
        let p1Color = this.patchColor1;
        let p2Color = this.patchColor2;
        fill(p2Color);
        console.log(midX + "," + midY);

        // Main line in the middle
        rect(midX - 50, midY - 2.5, patchWide + 50, 5);

        // Triangle looking down, in the middle
        triangle(midX - 10, midY, midX + 2.5, midY + 15, midX + 15, midY);
        // Triangle looking up, in the middle
        triangle(midX - 10, midY, midX + 2.5, midY - 15, midX + 15, midY);

        // Rectangle looking down, left of middle
        rect(midX - 25, midY + 2.5, patchWide - 45, 30);
        // End of rectangle
        rect(midX - 20, midY + 27.5, patchWide - 40, 5);

        // Rectangle looking down, most left of middle
        rect(midX - 45, midY + 2.5, patchWide - 45, 20);
        // End of rectangle
        rect(midX - 40, midY + 17.5, patchWide - 40, 5);

        // Rectangle looking down, right of middle
        rect(midX + 25, midY + 2.5, patchWide - 45, 30);
        // End of rectangle
        rect(midX + 15, midY + 27.5, patchWide - 40, 5);

        // Rectangle looking down, most right of middle
        rect(midX + 45, midY + 2.5, patchWide - 45, 20);
        // End of rectangle
        rect(midX + 35, midY + 17.5, patchWide - 40, 5);

        // Rectangle looking up, left of middle
        rect(midX - 25, midY - 2.5, patchWide - 45, -30);
        // End of rectangle
        rect(midX - 20, midY - 27.5, patchWide - 40, -5);
        // Rectangle looking up, most left of middle
        rect(midX - 45, midY - 2.5, patchWide - 45, -20);
        // End of rectangle
        rect(midX - 40, midY - 17.5, patchWide - 40, -5);

        // Rectangle looking up, right of middle
        rect(midX + 25, midY - 2.5, patchWide - 45, -30);
        // End of rectangle
        rect(midX + 15, midY - 27.5, patchWide - 40, -5);

        // Rectangle looking up, most right of middle
        rect(midX + 45, midY - 2.5, patchWide - 45, -20);
        // End of rectangle
        rect(midX + 35, midY - 17.5, patchWide - 40, -5);
      
    }
}